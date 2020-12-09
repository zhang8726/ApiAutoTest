class TestQuery:
    def test_01(self, db):  # 执行db前置
        print("查询：用例1")

    def test_02(self, login):  # 执行login前置
        print("查询：用例2")

    def test_03(self):
        print("查询：用例3")

    def test_04(self):  # 执行login、db后置
        print("查询：用例4")
