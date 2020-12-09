"""
pytest是一种测试框架，用来方便的组织测试脚本、生成报告，或与其他工具集成。
命名要求：
        1、测试文件已test_开头或_test结尾
        2、测试类已Test开头
        3、测试函数/方法一test_开头
执行：
    1、运行某个文件 pytest 脚本.py
    2、运行某个文件的某个用例  pytest 脚本.py::test_register_001
    3、运行生成测试报告 pytest 脚本.py --html=report.html
    4、多线程运行：pytest 脚本.py -n=3
    5、失败重执行：pytest 脚本.py --reruns=3
"""

import requests

url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"


def test_register_001():
    data = {
        "mobilephone": None,
        "pwd": '12345678'
    }
    r = requests.post(url, data=data)
    r = r.json()
    print(r)
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
