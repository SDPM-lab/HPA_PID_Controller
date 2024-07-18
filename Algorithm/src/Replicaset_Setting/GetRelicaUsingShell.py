import os
from google.cloud import container_v1
import subprocess

client = container_v1.ClusterManagerClient()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "/Users/tim/Desktop/Code/Python_File/Alo/impartantdata/gkeauth.json"
)


def get_replicaset_for_deployment(deployment_name, namespace):
    try:
        # Get deployment details
        deployment_info = subprocess.check_output(
            ["kubectl", "get", "deployment", deployment_name, "-n", namespace]
        )

        replicaset_info = subprocess.check_output(
            [
                "kubectl",
                "get",
                "replicasets",
                "-n",
                namespace,
            ]
        )

        print("ReplicaSet information:")
        print(deployment_info.decode("utf-8"))  # Decode the byte output to string

    except subprocess.CalledProcessError as e:
        print(f"Error executing kubectl command: {e}")


get_replicaset_for_deployment("frontend", "onlineshop")
