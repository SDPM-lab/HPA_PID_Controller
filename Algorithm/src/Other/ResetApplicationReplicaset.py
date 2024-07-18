# 引用
import os
from kubernetes import client, config


# 宣告
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "/Users/tim/Desktop/Code/Python_File/Alo/impartantdata/gkeauth.json"
)
config.load_kube_config()

deployment_list = []

def get_deployment_replicaset(NAMESPACE):
    global deployment_list
    api = client.AppsV1Api()
    all_deployments_data = api.list_namespaced_deployment(namespace=NAMESPACE)

    # 對於每個 Deployment，獲取其 Replicaset 數量
    for deployment in all_deployments_data.items:
        deployment_info = [
            deployment.metadata.name,
            deployment.status.replicas,
        ]
        deployment_list.append(deployment_info)
    return deployment_list

# 調整 Replicaset 數量
def scale_deployment_replicaset(deployment_name, namespace, replicaNum):
    ReplicaSet = int(replicaNum)
    if ReplicaSet < 1:
        ReplicaSet = 1

    api = client.AppsV1Api()

    TargetDeployment = api.read_namespaced_deployment(deployment_name, namespace)

    TargetDeployment.spec.replicas = ReplicaSet

    api.patch_namespaced_deployment_scale(deployment_name, namespace, TargetDeployment)
    print(deployment_name,"Replica Change to :", ReplicaSet)



# 輸出與執行
def main():
    
    deployment_list = []
    deployment_list = get_deployment_replicaset("onlineshop")
    for data in deployment_list:
        deployment_name = data[0]

        scale_deployment_replicaset(deployment_name, "onlineshop", 1)
            


if __name__ == "__main__":
    main()
