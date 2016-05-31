from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.kuwo.cn/yinyue/7105200?catalog=yueku2016")
print(driver.find_element_by_id('lrcContent').text)
driver.quit()
