"""
fixture的作用域：
1、默认是函数级别
2、函数级别 -> 模块级别 -> 类级别 -> Session级别
"""
"""
fixture的作用域：Session级别
公共方法放到conftest.py文件中，文件名字不能写错，pytest是根据文件名字找到对应方法的
1、conftest文件可以有多个
2、conftest放在SessionTest目录下，对SessionTest目录下的py文件以及其子目录下的py文件生效
3、conftest放在ApiAutoTest目录下，对整个工程生效
4、不用import
"""

import pytest


# 测试前置
# 整个执行过程，开始前执行前置，结束后执行后置
@pytest.fixture(scope='session')
def login():
    print("登录系统")  # yield之前是前置
    yield
    print("退出系统")  # yield之后是后置


@pytest.fixture(scope="session")
def db():
    print("连接数据库")
    yield
    print("断开数据库")
