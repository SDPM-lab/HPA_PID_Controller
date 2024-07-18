import os
import json
import subprocess
from google.cloud import container_v1

# 前面宣告
client = container_v1.ClusterManagerClient()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "/Users/tim/Desktop/Code/Python_File/Alo/impartantdata/gkeauth.json"
)


# 獲取 Deployment 資訊
def get_replicaset_for_deployment(deployment_name, namespace):
    try:

        # Get deployment details
        # kubectl get rs -o json -n onlineshop
        replicaset_info = subprocess.check_output(
            [
                "kubectl",
                "get",
                "rs",
                "-o",
                "json",
                "-n",
                namespace,
            ]
        )
        output_str = replicaset_info.decode("utf-8")
        data = json.loads(output_str)
        file_path = "/Users/tim/Desktop/Code/Python_File/Alo/impartantdata/GetData/RSResult.json"
        with open(file_path, "w") as file:
            json.dump(data, file)

        print(f"JSON檔案已儲存於 {file_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error executing kubectl command: {e}")


# 儲存成 Json

# 篩選 Deployment Json 檔案數據


# 嘗試修改 Deployment Replica 數量
def get_deployment_replica():
    with open(
        "/Users/tim/Desktop/Code/Python_File/Alo/impartantdata/GetData/RSResult.json"
    ) as file:
        # 轉 Python 物件
        data = json.load(file)

    # 處理資料
    itemdata = data["items"]
    datalen = len(itemdata)

    for i in range(datalen):
        print("Name:", data["items"][i]["metadata"]["name"])
        print("ReadyPod:", data["items"][i]["status"]["readyReplicas"])
        print("SetReplicas:", data["items"][i]["status"]["replicas"])
        print("-------------------")


# Function 執行
get_replicaset_for_deployment("frontend", "onlineshop")
get_deployment_replica()
