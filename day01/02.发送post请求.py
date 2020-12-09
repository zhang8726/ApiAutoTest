"""
发送post请求
"""

import requests

# 登录接口
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "13312345678",
    "pwd": "123456789"
}
# data 传表单参数，"content-type"："application/x-www-form-urlencoded"
r = requests.post(url, data=user)
print(r.text)

# 用data传表单参数
url = "http://www.httpbin.org/post"
user = {
    "mobilephone": "13312345678",
    "pwd": "123456789"
}
r = requests.post(url, data=user)
print(r.text)
print("-" * 30)
# 用json传参数，"Content-Type": "application/json"
r = requests.post(url, json=user)
print(r.text)

# 练习：充值接口，给注册的用户充值
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/recharge"
user = {
    "mobilephone": "13312345678",
    "amount": 500000
}
r = requests.post(url, data=user)
print(r.text)
# 取现
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/withdraw"
user = {
    "mobilephone": "13312345678",
    "amount": 500000
}
r = requests.post(url, data=user)
print(r.text)
# 投资、竞标
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/bidLoan"
user = {
    "mobileID": 1139,
    "pwd": "123456789",
    "loanId": 1234,
    "amount": 500000
}
r = requests.post(url, data=user)
print(r.text)