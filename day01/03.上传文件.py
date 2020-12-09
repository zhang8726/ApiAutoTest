"""
接口的功能是上传文件，比如上传头像，附件等
"""

import requests

url = "http://www.httpbin.org/post"
# 将本地的文件上传到服务器上
file1 = r"D:\workspace\ApiAutoTest\day01\test"
with open(file1, encoding='utf-8', mode='r') as f:
    # 字典，上传的文件：文件相关的参数组成的元组
    load = {
        "file": (file1, f)  # "text/plain"
    }
    r = requests.post(url, files=load)
    print(r.text)

file2 = r"D:\workspace\ApiAutoTest\day01\b.jpg"
with open(file2, mode='rb') as f:
    load = {
        "file2": (file2, f, "image/jpg")
    }
    r = requests.post(url, files=load)
    print(r.text)
# 一次上传多个文件，文本和图片一起上传
with open(file1, encoding='utf-8', mode='r') as f1:
    with open(file2, mode='rb') as f2:
        load = {
            "file1": (file1, f1),
            "file2": (file2, f2, "image/jpg")
        }
        r = requests.post(url, files=load)
        print(r.text)
