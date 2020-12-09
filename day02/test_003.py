"""
测试前置和后置：
    测试前置：测试环境的初始化、测试脚本执行前的准备
    测试后置：环境的清理
类级与方法级配合使用
    类级：前置在类开始前执行一次，后置在类结束后执行一次
    方法级：前置在每个方法开始前执行一次，后置在每个方法结束后执行一次
"""


class Test001:

    def setup_class(self):
        print("测试前置：class级别")

    def teardown_class(self):
        print("测试后置：class级别")

    def setup_method(self):
        print("测试前置：method级别")

    def teardown_method(self):
        print("测试后置：method级别")

    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")

    def test_03(self):
        print("test_03")
