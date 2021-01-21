import pytest
from appium import webdriver
import time


class TestDW():
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.house365.newhouse",
            "appActivity": "com.house365.newhouse.ui.SplashActivity",
            "platformVersion": "5.1.1",
            "unicodekeyBoard": True,
            "resetkeyBoard": True,
            "dontStopAppOnReset": True
            # "noReset": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id("com.house365.newhouse:id/tv_agree").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/"
                                          "android.widget.LinearLayout/android.widget.FrameLayout/"
                                          "android.widget.LinearLayout/android.widget.RelativeLayout/"
                                          "androidx.viewpager.widget.ViewPager/android.widget.ImageView").click()
        self.driver.find_element_by_accessibility_id("365淘房").click()
        self.driver.find_element_by_id("com.house365.newhouse:id/close").click()

    def teardown(self):
        self.driver.back()
        self.driver.back()
        # self.driver.quit()

    @pytest.mark.skip("此次测试不执行此用例")
    def test_search(self):
        print("搜索测试用例")

        """
         1、打开 淘房 APP
         2、点击首页的搜索输入框
         3、向搜索输入框里面输入“万科”
         4、向搜索结果里面选择“万科未来城”
         5、列表显示出带有“万科未来城”的搜索结果
        """
        self.driver.find_element_by_id("com.house365.newhouse:id/tv_search").click()
        self.driver.find_element_by_id("com.house365.newhouse:id/fragment_search_editText").send_keys("万科")
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.FrameLayout/"
                                          "android.widget.ListView/android.widget.LinearLayout[3]/"
                                          "android.widget.RelativeLayout/android.widget.LinearLayout/"
                                          "android.widget.TextView[1]").click()

        time.sleep(5)

    @pytest.mark.skip("此次测试不执行此用例")
    def test_xfxqy(self):
        print("新房详情页用例")

        """
             1、打开 淘房 APP
             2、点击首页新房icon
             3、新房列表页点击第一楼盘
            """
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.TabHost/"
                                          "android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.RelativeLayout/"
                                          "android.view.View[1]/android.widget.FrameLayout/"
                                          "android.widget.LinearLayout/android.widget.LinearLayout/"
                                          "android.widget.LinearLayout[1]/android.widget.GridView/"
                                          "android.widget.RelativeLayout[1]/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.house365.newhouse:id/close").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.RelativeLayout/"
                                          "android.widget.LinearLayout[3]/android.view.View/"
                                          "android.widget.RelativeLayout/android.view.View/"
                                          "android.widget.RelativeLayout/android.view.View/"
                                          "android.widget.RelativeLayout[1]/android.widget.RelativeLayout/"
                                          "android.widget.RelativeLayout/android.widget.LinearLayout/"
                                          "android.widget.LinearLayout[2]").click()

        # action = TouchAction(self.driver)
        # action.press(x=813,y=656).wait(100).move_to(x=767,y=502).release().perform()

    @pytest.mark.skip("此次测试不执行此用例")
    def test_esfxqy(self):
        print("二手房详情页用例")

        """
         1、打开 淘房 APP
         2、点击首页二手房icon
         3、列表页点击第一个房源
        """
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.TabHost/"
                                          "android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.RelativeLayout/"
                                          "android.view.View[1]/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.LinearLayout/android.widget.LinearLayout[1]/"
                                          "android.widget.GridView/android.widget.RelativeLayout[2]/"
                                          "android.widget.ImageView").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/"
                                          "android.widget.FrameLayout/android.widget.ScrollView/"
                                          "android.widget.ImageView").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.RelativeLayout/"
                                          "android.widget.LinearLayout[3]/android.view.View/android.view.View/"
                                          "android.widget.RelativeLayout/android.widget.RelativeLayout/"
                                          "android.view.View/android.widget.RelativeLayout[1]/"
                                          "android.widget.RelativeLayout/android.widget.RelativeLayout/"
                                          "android.widget.LinearLayout[2]").click()

    def test_myinfo(self):
        print("个人中心登录用例")

        """
         1、打开 淘房 APP
         2、点击我的，进去到个人中心页面
         3、点击登录，输入用户名，密码
         4、点击登录按钮
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("注册")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("账号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.house365.newhouse:id/'
                                                        'et_input_phone")').send_keys("13182855160")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.house365.newhouse:id/'
                                                        'et_login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.house365.newhouse:id/'
                                                        'btn_user_login")').click()


if __name__ == '__main__':
    pytest.main()
