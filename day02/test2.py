import pytest
import requests
import random


@pytest.fixture(params=[{"data": {"mobilephone": None, "pwd": '12345678'},
                         "expect": {"status": 0, "code": '20103', "msg": '手机号不能为空'}},
                        {"data": {"mobilephone": '1234567890', "pwd": '12345678'},
                         "expect": {"status": 0, "code": '20109', "msg": '手机号码格式不正确'}},
                        {"data": {"mobilephone": '11111111111', "pwd": '12345678'},
                         "expect": {"status": 0, "code": '20109', "msg": '手机号码格式不正确'}},
                        {"data": {"mobilephone": '123412341234', "pwd": '12345678'},
                         "expect": {"status": 0, "code": '20109', "msg": '手机号码格式不正确'}},
                        {"data": {"mobilephone": '13112345678', "pwd": '12345678'},
                         "expect": {"status": 0, "code": '20110', "msg": '手机号码已被注册'}},
                        {"data": {"mobilephone": '131%s' % random.randint(10000000, 99999999), "pwd": '12345'},
                         "expect": {"status": 0, "code": '20108', "msg": '密码长度必须为6~18'}}
                        ])
def login_data(request):  # 参数request是固定的，不能写成其他
    return request.param  # 使用request.param返回每组数据


# 测试逻辑（测试步骤）
# 登录功能测试脚本
def test_login(login_data):
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
    print()
    print("测试登录功能，测试数据为：", login_data['data'])
    print("测试登录功能，预期结果为：", login_data['expect'])
    r = requests.post(url, data=login_data['data'])
    print(r.json())
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['msg'] == login_data['expect']['msg']
