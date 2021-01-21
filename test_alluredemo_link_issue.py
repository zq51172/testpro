import allure
import pytest

@allure.link("http://www.baidu.com",name="链接")
def  test_with_link():
    print("这是一条加了链接的用例")
    pass

