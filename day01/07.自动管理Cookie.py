"""
自动管理Cookie
通过requests.session 自动管理Cookies
"""

import requests

s = requests.session()

# 登录百格
url = 'https://www.bagevent.com/user/login'
user = {
    "access_type": "1",
    "loginType": "1",
    "emailLoginWay": "0",
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindmeBox": "on",
    "remindme": "1"
}
r = s.post(url, data=user)
print("登录前：", s.cookies)
# print(r.text)
# 获取账号信息
url = "https://www.bagevent.com/account/dashboard"
s.get(url)
print("登录后：", s.cookies)
