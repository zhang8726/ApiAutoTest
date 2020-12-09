"""
脚本层的一些公关方法
"""
import pytest
from ZongHe.caw import DataRead
from ZongHe.caw.BaseRequests import BaseRequests
import sys

sys.path.append(DataRead.get_project_path())


# 从环境文件读取url
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(r'data_env\env.ini', "url")


# 创建一个BaseRequests的实例
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()


# 从环境文件中读取db信息
@pytest.fixture(scope='session')
def db():
    # 读取出来是字符串，需要的是字典，需要解析
    info = DataRead.read_ini(r'data_env\env.ini', "db")
    return eval(info)  # 将字符串解析从字典
