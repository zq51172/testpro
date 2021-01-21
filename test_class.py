# conftest.py
import pytest
import time
from selenium import webdriver

@pytest.fixture(scope='session')
def driver(request):
    driver = webdriver.Firefox()
    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver

@pytest.fixture()
def start(driver):
    print('打开百度')
    driver.get('https://www.baidu.com')
    time.sleep(5)

# test_class.py
import pytest
import time


def test_1(driver,start):
    print('搜索python')
    driver.find_element_by_id('kw').send_keys('python')
    driver.find_element_by_id('su').click()
    time.sleep(5)
def test_2(driver,start):
    print('搜索地图')
    driver.find_element_by_id('kw').send_keys('地图')
    driver.find_element_by_id('su').click()
    time.sleep(5)

if __name__ == '__main__':
    pytest.main(['-q', 'test_class.py'])

# test_classs.py
import pytest


class Testclass:

    def test_1(self,driver):
        driver.get('https://www.baidu.com')
        print('打开百度')
    def test_2(self,driver):
        driver.get('https://i.qq.com/')
        print('打开空间')
if __name__ == '__main__':
    pytest.main(['-q', 'test_classs.py'])