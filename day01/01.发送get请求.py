"""
使用requests发送get请求
"""

import requests  # 导入包

# 发送一个get请求
# r = requests.get("http://www.baidu.com/s?wd=参数")
# print(r.text)

# list 获取用户列表。 http://192.168.150.54:8089/
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/list"
r = requests.get(url)  # 发送请求
print(r.json())
r = r.json()
assert r['status'] == 1  # 对结果进行检查
assert r['code'] == '10001'
assert r['msg'] == '获取用户列表成功'

# get请求带参数。方式1：拼接到url后面。？参数名1=参数值1&参数名2=参数值2
# 注册接口
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=13312345678&pwd=123456789"
r = requests.get(url)
print(r.json())
r = r.json()
assert r['status'] == 0  # 对结果进行检查
assert r['code'] == '20110'
assert r['msg'] == '手机号码已被注册'

# 登录接口
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login?mobilephone=13312345678&pwd=123456789"
r = requests.get(url)
print(r.json())

# get请求带参数。方式2：使用params参数
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13312345678",
    "pwd": "123456789"
}
r = requests.get(url, params=user)
print(r.json())
r = r.json()
assert r['status'] == 0  # 对结果进行检查
assert r['code'] == '20110'
assert r['msg'] == '手机号码已被注册'

# 练习：
# 接口功能：查询手机号码归属地
# 接口地址：https://tcc.taobao.com/cc/json/mobile_tel_segment.htm
# 方法：get
# 参数名：tel
# 参数值：手机号码
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
tel = {
    "tel": "18829298848"
}
r = requests.get(url, params=tel)
print(r.text)
print(type(r))
print(r.status_code)  # 状态码
print(r.reason)  # 状态信息
print(r.cookies)  # cookies
print(r.encoding)  # 编码方式
print(r.headers)  # 响应头

# 发送请求时，带请求头
# 有些网站对自动化发出的请求不处理或处理结果与实际不一致
# 通过设置请求头，伪装成浏览器发的请求
# httpbin是一个测试网站，方式的请求，这个网站将请求转成json格式的返回
url = "http://www.httpbin.org/get?user=root&pwd=123456"
r = requests.get(url)
print(r.text)
# 使用requests发送的请求，"User-Agent": "python-requests/2.24.0"
# 设置请求头
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.183 Safari/537.36 "
}
r = requests.get(url, headers=head)
print(r.text)
