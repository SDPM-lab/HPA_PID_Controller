import json

# 開啟JSON檔案,讀取模式
with open(
    "/Users/tim/Desktop/Code/Python_File/Alo/impartantdata/GetData/RSResult.json"
) as file:

    # 使用json.load()將文件內容轉為Python物件
    data = json.load(file)

# 處理資料
itemdata = data["items"]
datalen = len(itemdata)

for i in range(datalen):
    print("Name:", data["items"][i]["metadata"]["name"])
    print("ReadyPod:", data["items"][i]["status"]["readyReplicas"])
    print("SetReplicas:", data["items"][i]["status"]["replicas"])
    print("-------------------")
