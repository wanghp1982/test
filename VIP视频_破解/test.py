import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
//a[@id="j-src-btn"]/@href
"""

driver = webdriver.Chrome()
driver.get("http://music.ifkdy.com/")
driver.find_element_by_xpath('//input[@id="j-input"]').send_keys('Lovebird')
driver.find_element_by_xpath('//label[@class="am-radio-inline"][2]').click()
WebDriverWait(driver, 10).find_element_by_xpath('//button[@id="j-submit"]').click()
html = etree.HTML(driver.page_source)
driver.close()
music_url = html.xpath('//a[@id="j-src-btn"]/@href')

print(music_url)
