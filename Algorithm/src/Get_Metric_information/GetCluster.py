import os
from google.cloud import container_v1

client = container_v1.ClusterManagerClient()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "/Path/to/Your/impartantdata/gkeauth.json"
)

request = container_v1.GetClusterRequest(
    project_id="Project-id",
    zone="Zone",
    cluster_id="cluster_id",
)

response = client.get_cluster(request=request)
print(response)
