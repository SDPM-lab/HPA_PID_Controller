from kubernetes import client, config
from kubernetes.client import CustomObjectsApi

# 加载 Kubernetes 配置
config.load_kube_config()

# 定义 API 客户端
custom_api = CustomObjectsApi()

namespace = 'onlineshop'  # 请根据实际情况修改命名空间

# 获取 Pod 的指标
api_response = custom_api.list_namespaced_custom_object(
    group="metrics.k8s.io",
    version="v1beta1",
    namespace=namespace,
    plural="pods"
)
total_cpu_usage = 0
    
# 解析并打印 CPU 使用率
for item in api_response['items']:
    pod_name = item['metadata']['name']
    for container in item['containers']:
        cpu_usage = container['usage']['cpu']
        if pod_name == 'frontend-798bc75654-rjjxg':
            print(f"Pod: {pod_name}, Container: {container['name']}, CPU Usage: {cpu_usage}")
            

        


