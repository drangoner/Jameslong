from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://y.qq.com/#type=song&mid=001nWoME0kaG55&tpl=yqq_song_detail")

print(driver.find_element_by_id('lrc_content').text)
driver.quit()
