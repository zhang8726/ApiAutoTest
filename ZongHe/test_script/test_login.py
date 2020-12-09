"""
登录接口测试脚本
"""
import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member, DbOp


@pytest.fixture(params=DataRead.read_yaml("data_case/login_setup.yaml"))
def setup_data(request):
    return request.param


@pytest.fixture(params=DataRead.read_yaml("data_case/login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture()
def register(setup_data, url, db, baserequests):
    # 注册用户
    print(f"测试前置数据：{setup_data}")
    # 获取手机号
    mobile = setup_data['casedata']['mobilephone']
    # 下发注册的请求
    # DbOp.delete_user(db, mobile)
    r = Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 删除用户
    DbOp.delete_user(db, mobile)


@pytest.mark.usefixtures("register")
def test_login(login_data, url, db, baserequests):
    print(f"测试数据：{login_data}")
    # 获取手机号
    mobile = login_data['casedata']['mobilephone']
    # 下发登录请求
    # DbOp.delete_user(db, mobile)
    r = Member.login(url, baserequests, login_data['casedata'])
    print(r.json())
    # 校验结果
    assert r.json()['msg'] == login_data['expect']['msg']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['code'] == login_data['expect']['code']
