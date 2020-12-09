"""
fixture的作用域：
1、默认是函数级别
2、函数级别 -> 模块级别 -> 类级别 -> Session级别
"""

# fixture的作用域：类级别

import pytest


# 测试前置
@pytest.fixture(scope='class')
def login():
    print("登录系统")  # yield之前是前置
    yield
    print("退出系统")  # yield之后是后置


@pytest.fixture(scope="class")
def db():
    print("连接数据库")
    yield
    print("断开数据库")


class TestQuery:
    def test_01(self, db):  # 执行db前置
        print("查询：用例1")

    def test_02(self, login):  # 执行login前置
        print("查询：用例2")

    def test_03(self):
        print("查询：用例3")

    def test_04(self):  # 执行login、db后置
        print("查询：用例4")


class TestAdd:
    def test_01(self, db, login):  # 执行db、login前置
        print("添加：用例1")

    def test_02(self):
        print("添加：用例2")

    def test_03(self):
        print("添加：用例3")

    def test_04(self):  # 执行login、db后置
        print("添加：用例4")
