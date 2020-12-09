"""
mock：
1、接口测试的测试场景比较难模拟，需要大量的工作才能做好
2、该接口的测试，依赖其他模块的接口，依赖的接口尚未开发完成
测试条件不充分时，该怎么开展接口测试？
使用mock模拟接口的返回值
"""
import requests
from unittest import mock

"""
支付接口：http://www.zhifu.com/
方法：post
参数：{"订单号":"12345","支付金额":"20.21","支付方式":"支付宝/微信/银行卡"}
返回值：{"code":"200","msg":"支付成功"}、{"code":"201","msg":"支付失败"}
接口尚未开发完成
"""


class Pay:
    def zhifu(self, data):
        r = requests.post("http://www.zhifu.com/", data=data)
        return r.json()


def test_01():
    pay = Pay()
    # 通过mock模拟接口的返回值
    pay.zhifu = mock.Mock(return_value={"code": "200", "msg": "支付成功"})
    canshu = {"订单号": "12345", "支付金额": "20.21", "支付方式": "支付宝"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == '支付成功'


def test_02():
    pay = Pay()
    # 通过mock模拟接口的返回值
    pay.zhifu = mock.Mock(return_value={"code": "201", "msg": "支付失败"})
    canshu = {"订单号": "12345", "支付金额": "-20.21", "支付方式": "支付宝"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == '支付失败'


# 模块名.类名.方法名
@mock.patch("test_001.Pay.zhifu", return_value={"code": "200", "msg": "支付成功"})
def test_03(mock_pay):
    pay = Pay()
    canshu = {"订单号": "12345", "支付金额": "21120.21", "支付方式": "支付宝"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == '支付成功'


class WithDraw:
    def withdraw(self, data):
        r = requests.post("http://192.168.150.54:8089/futureloan/mvc/api/member/withdraw", data=data)
        return r.json()


# 取现接口未实现，写一个取现成功的用例
def test_withdraw_01():
    wd = WithDraw()
    # 通过mock模拟接口的返回值
    wd.withdraw = mock.Mock(return_value={"status": 1, "code": "20001", "msg": "取现成功"})
    canshu = {"mobilephone": "13398761234", "amount": "22340.21"}
    r = wd.withdraw(canshu)
    print(r)
    assert r['msg'] == '取现成功'


@mock.patch("test_001.WithDraw.withdraw", return_value={"status": 0, "code": "20111", "msg": "取现失败"})
def test_withdraw_02(mock_wd):
    wd = WithDraw()
    canshu = {"mobilephone": "13398761234", "amount": "-22340.21"}
    r = wd.withdraw(canshu)
    print(r)
    assert r['msg'] == '取现失败'
