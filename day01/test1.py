import random

import requests

# sign_001
# 验证用户使用空手机号码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": None,
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '手机号不能为空'

# sign_002
# 验证用户使用过短手机号码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '1234567890',
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

# sign_003
# 验证用户使用格式错误手机号码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '11111111111',
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

# sign_004
# 验证用户使用过长的手机号码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '123412341234',
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

# sign_005
# 验证用户使用已注册的手机号码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '13112345678',
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20110'
assert r['msg'] == '手机号码已被注册'

# sign_006
# 验证用户使用长度为5的密码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '131%s'%random.randint(10000000, 99999999),
    "pwd": '12345'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20108'
assert r['msg'] == '密码长度必须为6~18'

# sign_007
# 验证用户使用长度为6的密码注册，注册成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '131%s' % random.randint(10000000, 99999999),
    "pwd": '123456'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '注册成功'

# sign_008
# 验证用户使用长度为18的密码注册，注册成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '131%s' % random.randint(10000000, 99999999),
    "pwd": '123456789987654321'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '注册成功'

# sign_009
# 验证用户使用长度为19的密码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '131%s' % random.randint(10000000, 99999999),
    "pwd": '1234567890987654321'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20108'
assert r['msg'] == '密码长度必须为6~18'

# sign_010
# 验证用户使用空密码注册，注册异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '131%s' % random.randint(10000000, 99999999),
    "pwd": None
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '密码不能为空'

# sign_011
# 验证用户使用合法手机号码、密码注册，注册成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '131%s' % random.randint(10000000, 99999999),
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '注册成功'


# login_001
# 验证用户使用空密码登录，登录异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": '13112345678',
    "pwd": None
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '密码不能为空'

# login_002
# 验证用户使用空手机号码登录，登录异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": None,
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '手机号不能为空'

# login_003
# 验证用户使用过短手机号码登录，登录异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": '1311234567',
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

# login_004
# 验证用户使用格式错误手机号码登录，登录异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": '11112345678',
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

# login_005
# 验证用户使用过长手机号码登录，登录异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": '131123456780',
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

# login_006
# 验证用户使用长度为5密码登录，登录异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": '13112345678',
    "pwd": '12345'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

# login_007
# 验证用户使用长度为6密码登录，登录成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": '13112345678',
    "pwd": '123456'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '登录成功'

# login_008
# 验证用户使用长度为18密码登录，登录成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": '13912345678',
    "pwd": '123456789987654321'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '登录成功'

# login_009
# 验证用户使用长度为19密码登录，登录异常
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": '13112345678',
    "pwd": '1234567890987654321'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或密码错误'

# login_010
# 验证用户使用正确手机号码、密码登录，登录成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": '13112345679',
    "pwd": '12345678'
}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '登录成功'
