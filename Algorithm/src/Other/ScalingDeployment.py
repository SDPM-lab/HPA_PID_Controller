from kubernetes import client, config

config.load_kube_config()

v1 = client.AppsV1Api()

number_of_replicas = 1

patch = {"spec": {"replicas": number_of_replicas}}

v1.patch_namespaced_deployment_scale(
    name="frontend", namespace="onlineshop", body=patch
)
