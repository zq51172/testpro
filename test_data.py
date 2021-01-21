import pytest
import yaml

class TestData:
    def test_data1(self):
        a=10
        b=20
        # assert "1" ==2
        print(a + b)

    @pytest.mark.xfail
    def test_data2(self):
        a = 11
        b = 20
        print(a+b)
        assert "1"=="2"
    @pytest.mark.skip("此次用例不执行")
    def test_data3(self):
        a = 12
        b = 20
        print(a+b)

    @pytest.mark.print
    def test_data4(self):
        a = 10
        b = 20
        print(a + b)

    @pytest.mark.print
    def test_data5(self):
        a = 11
        b = 20
        print(a + b)

        assert "1" == "2"
    @pytest.mark.print
    def test_data6(self):
        a = 12
        b = 20
        print(a + b)
# class TestData():
#       @pytest.mark.parametrize("a,b",[(10,20),(10,5),(3,9)])
#       def test_data(self,a,b):
#           print(a+b)

# class TestData():
#       @pytest.mark.parametrize(("a","b"),[(10,20),(10,5),(3,9)])
#       def test_data(self,a,b):
#           print(a+b)


# class TestData():
#     @pytest.mark.parametrize(["a", "b"], [(10, 20), (10, 5), (3, 9)])
#     def test_data(self, a, b):
#         print(a + b)


# class TestData():
#     @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("D:\\testpro\\data.yaml")))
#     def test_data(self, a, b):
#         print(a + b)

# # class TestData():
# @pytest.mark.parametrize("test_input, expected",[("3+5",8),("2+5",7),("7+7",14)] )
# def test_eval(test_input, expected):
#          assert eval(test_input) == expected

if __name__ =="__main__":
    pytest.main("-v -x TestData")
#     pytest.main(["-v","-s","TestDate"])


# #参数组合
# @pytest.mark.parametrize("x",[1,2])
# @pytest.mark.parametrize("y",[8,10,12])
# def test_foo(x,y):
#     print(f"测试数据组合x:{x},y:{y}")