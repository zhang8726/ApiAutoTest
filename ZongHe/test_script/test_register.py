"""
注册的测试脚本
"""
import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member, DbOp


# 测试数据
@pytest.fixture(params=DataRead.read_yaml(r"data_case/register_fail.yaml"))
def fail_data(request):
    return request.param


@pytest.fixture(params=DataRead.read_yaml(r"data_case/register_pass.yaml"))
def pass_data(request):
    return request.param


# 测试逻辑
def test_register_fail(fail_data, url, baserequests):
    print(f"测试数据：{fail_data}")
    # 下发注册的请求
    r = Member.register(url, baserequests, fail_data['data'])
    # 校验结果
    assert r.json()['msg'] == fail_data['expect']['msg']
    assert r.json()['status'] == fail_data['expect']['status']
    assert r.json()['code'] == fail_data['expect']['code']


def test_register_pass(pass_data, url, db, baserequests):
    print(f"测试数据：{pass_data}")
    # 获取手机号
    mobile = pass_data['data']['mobilephone']
    # 下发注册的请求
    # DbOp.delete_user(db, mobile)
    r = Member.register(url, baserequests, pass_data['data'])
    # 校验结果。1、检查响应与预期结果一致
    assert r.json()['msg'] == pass_data['expect']['msg']
    assert r.json()['status'] == pass_data['expect']['status']
    assert r.json()['code'] == pass_data['expect']['code']
    # 校验结果。2、检查系统中用户注册成功
    # 方法1：查找用户列表
    r = Member.list(url, baserequests)
    assert mobile in r.text
    # flag = False
    # for i in range(0, len(r.json()['data'])):
    #     if mobile == r.json()['data'][i]['mobilephone']:
    #         flag = True
    # assert flag == True
    # 方法2：在数据库中查找
    a = DbOp.select_user(db, mobile)
    assert len(a) == 1
    # 清理环境：删除注册用户
    DbOp.delete_user(db, mobile)


def test_register_again(pass_data, url, db, baserequests):
    print(f"测试数据：{pass_data}")
    # 获取手机号
    mobile = pass_data['data']['mobilephone']
    # DbOp.delete_user(db, mobile)
    # 下发注册的请求
    r = Member.register(url, baserequests, pass_data['data'])
    # 校验结果。1、检查响应与预期结果一致
    assert r.json()['msg'] == pass_data['expect']['msg']
    assert r.json()['status'] == pass_data['expect']['status']
    assert r.json()['code'] == pass_data['expect']['code']
    # 校验结果。2、检查系统中用户注册成功
    r = Member.list(url, baserequests)
    assert mobile in r.text

    # 重复注册
    # 下发注册的请求
    r = Member.register(url, baserequests, pass_data['data'])
    # 校验结果。1、检查响应与预期结果一致
    assert r.json()['msg'] == '手机号码已被注册'
    assert r.json()['status'] == 0
    assert r.json()['code'] == '20110'
    # 校验结果。2、检查系统中用户注册成功
    r = Member.list(url, baserequests)
    assert mobile in r.text

    # 清理环境：删除注册用户
    DbOp.delete_user(db, mobile)
