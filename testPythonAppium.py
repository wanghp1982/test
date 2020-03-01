from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# appium服务监听地址
server='http://localhost:4723/wd/hub'
# app启动参数
desired_caps={
  "platformName": "Android",
  "deviceName": "vivo_X9",
  "appPackage": "com.tencent.mm",
  "appActivity": ".ui.LauncherUI"
}

# 驱动
driver = webdriver.Remote(server,desired_caps)
wait = WebDriverWait(driver,30)
# 获取登录按钮
login_btn = wait.until(EC.presence_of_element_located((By.ID,"com.tencent.mm:id/drp")))
# 点击登录按钮
login_btn.click()
# 获取手机号文本框
phone_text = wait.until(EC.presence_of_element_located((By.ID,"com.tencent.mm:id/ji")))
# 填写手机号文本框
phone_text.send_keys("18888888888")