"""
member模块
"""


def register(url, baserequests, data):
    """
    注册接口
    :param url: 环境信息
    :param baserequests: BaseRequests的实例
    :param data: 注册的测试数据
    :return: 响应信息
    """
    url = url + "futureloan/mvc/api/member/register"
    r = baserequests.post(url, data=data)
    return r


def login(url, baserequests, data):
    """
    登录接口
    :param url: 环境信息
    :param baserequests: BaseRequests的实例
    :param data: 登录的测试数据
    :return: 响应信息
    """
    url = url + "futureloan/mvc/api/member/login"
    r = baserequests.post(url, data=data)
    return r


def list(url, baserequests):
    """
    获取用户列表接口
    :param url: 环境信息
    :param baserequests: BaseRequests的实例
    :return: 响应信息
    """
    url = url + "futureloan/mvc/api/member/list"
    r = baserequests.post(url)
    return r


if __name__ == '__main__':
    from ZongHe.caw.BaseRequests import BaseRequests

    b = BaseRequests()
    data = {"mobilephone": '17792930289', "pwd": "123456"}
    r = register("http://jy001:8081/", b, data)
    print(r.text)
    r = list("http://jy001:8081/", b)
    print(r.text)
