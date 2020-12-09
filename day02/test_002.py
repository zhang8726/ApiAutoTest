import requests

"""
测试前置和后置：
    测试前置：测试环境的初始化、测试脚本执行前的准备
    测试后置：环境的清理
模块级与函数级配合使用
    模块级：前置在模块开始前执行一次，后置在模块结束后执行一次
    函数级：前置在每个函数开始前执行一次，后置在每个函数结束后执行一次
"""


def setup_module():
    print("测试前置：module级别")


def teardown_module():
    print("测试后置：module级别")


def setup_function():
    print("测试前置：function级别")


def teardown_function():
    print("测试后置：function级别")


url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"


def test_register_001():
    data = {
        "mobilephone": None,
        "pwd": '12345678'
    }
    r = requests.post(url, data=data)
    r = r.json()
    assert r['status'] == 0
    assert r['code'] == '20103'
    assert r['msg'] == '手机号不能为空'


def test_register_002():
    data = {
        "mobilephone": '1234567890',
        "pwd": '12345678'
    }
    r = requests.post(url, data=data)
    r = r.json()
    assert r['status'] == 0
    assert r['code'] == '20109'
    assert r['msg'] == '手机号码格式不正确'


def test_register_003():
    data = {
        "mobilephone": '11111111111',
        "pwd": '12345678'
    }
    r = requests.post(url, data=data)
    r = r.json()
    assert r['status'] == 0
    assert r['code'] == '20109'
    assert r['msg'] == '手机号码格式不正确'
