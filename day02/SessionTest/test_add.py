class TestAdd:
    def test_01(self, db, login):  # 执行db、login前置
        print("添加：用例1")

    def test_02(self):
        print("添加：用例2")

    def test_03(self):
        print("添加：用例3")

    def test_04(self):  # 执行login、db后置
        print("添加：用例4")
