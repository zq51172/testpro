
from selenium import webdriver

import time

def main():
    b=webdriver.Firefox()
    b.get('https://www.baidu.com')
    time.sleep(5)
    b.maximize_window()
    time.sleep(3)
    b.quit()


if __name__ == '__main__':
    main()