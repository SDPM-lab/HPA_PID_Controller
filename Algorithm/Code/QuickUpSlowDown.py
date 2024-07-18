import math
import time
import os
from kubernetes import client, config
from kubernetes.client import CustomObjectsApi

# GKE 用憑證認證
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "/path/to/impartantdata/gkeauth.json"
)
config.load_kube_config()


def scale_deployment_replicaset(deployment_name, namespace, replicaNum):
    ReplicaSet = int(replicaNum)
    if ReplicaSet < 1:
        ReplicaSet = 1

    api = client.AppsV1Api()

    TargetDeployment = api.read_namespaced_deployment(deployment_name, namespace)

    TargetDeployment.spec.replicas = ReplicaSet

    api.patch_namespaced_deployment_scale(deployment_name, namespace, TargetDeployment)


def get_deployment_replicaset(NAMESPACE):
    global deployment_list
    api = client.AppsV1Api()
    all_deployments_data = api.list_namespaced_deployment(namespace=NAMESPACE)

    for deployment in all_deployments_data.items:
        deployment_info = [
            deployment.metadata.name,
            deployment.spec.replicas,
        ]
        deployment_list.append(deployment_info)
    return deployment_list



RatioTarget = 70
Threshold = 0.10

MinReplicaSet = 1
MaxReplicaSet = 30


def get_cpu_percent(deployment_name,NowReadyReplicaSet):

    custom_api = CustomObjectsApi()
    namespace = 'onlineshop'
    total_cpu_usage = 0

    api_response = custom_api.list_namespaced_custom_object(
        group="metrics.k8s.io",
        version="v1beta1",
        namespace=namespace,
        plural="pods"
    )

    for item in api_response['items']:
        deployment = item['metadata'].get('labels', {}).get('app')
        if deployment == deployment_name:
            for container in item['containers']:
                cpu_usage = container['usage']['cpu']
                
                if cpu_usage.endswith('n'):
                    cleaned_cpu_usage = int(cpu_usage[:-1])
                elif cpu_usage.endswith('u'):
                    cleaned_cpu_usage = int(cpu_usage[:-1]) * 1_000
                elif cpu_usage.endswith('m'):
                    cleaned_cpu_usage = int(cpu_usage[:-1]) * 1_000_000
                else:
                    cleaned_cpu_usage = int(float(cpu_usage) * 1_000_000_000)

                integer_cpu_usage = int(cleaned_cpu_usage)
                total_cpu_usage += integer_cpu_usage

    total_cpu_usage_m = round(total_cpu_usage / 1000000)

    avg_cpu_usage = round(total_cpu_usage_m / NowReadyReplicaSet)
    
    
    
    return avg_cpu_usage


def show_result(NowMetric,Desire_ReplicaSet):
    
    print("Deployment 名稱：", deployment_name)
    print(f"平均利用率 {NowMetric} %,調整前是 {beforeReplicaset} 個,調整後是 {Desire_ReplicaSet} 個")
    

def check_scale_and_way(value, threshold):
    if value > 1 + threshold:
        return 1
    elif value < 1 - threshold:
        return -1
    else:
        return 0


def check_replicaset_range(nowReplicaSet, minReplicaSet, maxReplicaSet):
    if nowReplicaSet > maxReplicaSet:
        nowReplicaSet = maxReplicaSet
        return maxReplicaSet
    elif nowReplicaSet < minReplicaSet:
        nowReplicaSet = minReplicaSet
        return minReplicaSet
    else:
        return nowReplicaSet


def new_pid_alo(NowMetric, RatioTarget, Threshold):
    global NowReadyReplicaSet
    ratio = NowMetric / RatioTarget
    how_to_scale = check_scale_and_way(ratio, Threshold)
    Desire_ReplicaSet = 0

    if how_to_scale == 1:
        NowReadyReplicaSet = quick_up(NowReadyReplicaSet, ratio)
        Desire_ReplicaSet = check_replicaset_range(
            NowReadyReplicaSet, MinReplicaSet, MaxReplicaSet
        )
        
    elif how_to_scale == -1:
        NowReadyReplicaSet = slow_down(NowReadyReplicaSet, ratio)
        Desire_ReplicaSet = check_replicaset_range(
            NowReadyReplicaSet, MinReplicaSet, MaxReplicaSet
        )
        
    else:
        Desire_ReplicaSet = NowReadyReplicaSet
    scale_deployment_replicaset(deployment_name, 'onlineshop', Desire_ReplicaSet)
    
    # Check Result
    return show_result(NowMetric,Desire_ReplicaSet)


def quick_up(NowReadyReplicaSet, ratio):

    NowReadyReplicaSet = math.ceil(ratio * NowReadyReplicaSet) + 2

    return NowReadyReplicaSet


def slow_down(NowReadyReplicaSet, ratio):

    NewReplicaSet = math.ceil((1/3) * NowReadyReplicaSet + (2/3) * NowReadyReplicaSet * ratio)
    
    return NewReplicaSet


def main(deployment_name,NowReadyReplicaSet):

    NowMetric = get_cpu_percent(deployment_name,NowReadyReplicaSet)

    new_pid_alo(NowMetric, RatioTarget, Threshold)



if __name__ == "__main__":
    
    StepTime = 1
    while True:
        
        deployment_list = []
        deployment_list = get_deployment_replicaset("onlineshop")

        for data in deployment_list:
            deployment_name = data[0]
            NowReadyReplicaSet = data[1]
            beforeReplicaset = NowReadyReplicaSet
        
        if deployment_name != "loadgenerator":
            main(deployment_name,NowReadyReplicaSet)   

        time.sleep(35)
        StepTime += 1


     
