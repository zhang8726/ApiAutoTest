"""
mark标记：
1、跳过用例，某个版本有缺陷导致脚本执行不通过，可以跳过该用例，待缺陷解决后再继续执行
2、脚本越写越多，如果想执行其中的一部分脚本，使用自定义标记
    全量的脚本，挑选一部分作为冒烟测试的脚本，只想执行冒烟测试这一部分的脚本
多个自定义标记时，可以用与、或、非组合：
    -m=smoke  执行smoke标记的用例
    -m="smoke and api"  执行既有smoke又有api标记的用例
    -m="smoke or api"  执行有smoke或者api标记的用例
    -m="not smoke"  执行非smoke标记的用例
"""

import pytest


@pytest.mark.smoke  # 自定义标记.smoke
def test_01():
    print("测试用例1")


@pytest.mark.skip("跳过的原因：尚未支持的功能，暂不执行，待实现后再执行")
def test_02():
    print("测试用例2")


@pytest.mark.smoke
def test_03():
    print("测试用例3")


@pytest.mark.api
def test_04():
    print("测试用例4")


@pytest.mark.api
class TestMark:
    def test_11(self):
        print("测试用例11")

    @pytest.mark.smoke
    def test_12(self):
        print("测试用例12")

    def test_13(self):
        print("测试用例13")

    @pytest.mark.smoke
    def test_14(self):
        print("测试用例14")

    def test_15(self):
        print("测试用例15")
