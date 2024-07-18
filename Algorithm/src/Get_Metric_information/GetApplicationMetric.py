"""
n (nano):
1n = 0.000000001m
1000000000n= 

u (micro):
1u = 0.000001m
k (kilo):
1k = 1000m
K (kibibyte):
1K = 1024m
"""


from kubernetes import client, config
from kubernetes.client import CustomObjectsApi
import time
def get_cpu_percent(deployment_name):

    config.load_kube_config()
    custom_api = CustomObjectsApi()
    namespace = 'onlineshop'  # 根據實際情況修改
    
    # 定義總 CPU 使用率
    total_cpu_usage = 0
    

    api_response = custom_api.list_namespaced_custom_object(
        group="metrics.k8s.io",
        version="v1beta1",
        namespace=namespace,
        plural="pods"
    )


    for item in api_response['items']:
        pod_name = item['metadata']['name']
        deployment = item['metadata'].get('labels', {}).get('app')
        if deployment == deployment_name:
            for container in item['containers']:
                cpu_usage = container['usage']['cpu']
                #區分單位
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

    final_cpu_usage = round(total_cpu_usage / 1000000)

    print(f"Final CPU Usage: {final_cpu_usage}")

def main(step):
    deployment_name = 'frontend'
    print("第",step,"次抓取")
    get_cpu_percent(deployment_name)

if __name__ == "__main__":
    step = 0
    while True:
        main(step)
        time.sleep(3)
        step += 1
        
        
