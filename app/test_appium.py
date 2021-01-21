from appium import webdriver
import time

desire_cap ={
    "platformName": "Android",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.house365.newhouse",
    "appActivity": "com.house365.newhouse.ui.SplashActivity",
    "platformVersion": "5.1.1",
    "unicodekeyBoard": True,
    "resetkeyBoard": True,
    # "dontStopAppOnReset": True
    # "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
driver.implicitly_wait(10)

driver.find_element_by_id("com.house365.newhouse:id/tv_agree").click()

el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.ImageView")
el2.click()

driver.find_element_by_accessibility_id("365淘房").click()

# time.sleep(3)

driver.find_element_by_id("com.house365.newhouse:id/tv_search").click()
driver.find_element_by_id("com.house365.newhouse:id/fragment_search_editText").send_keys("万科")

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]").click()

time.sleep(5)
#driver.quit()