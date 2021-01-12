from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_bar = driver.find_element_by_xpath(
    '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_bar.clear()
search_bar.send_keys('GNVageesh')
search_bar.send_keys(Keys.RETURN)
sleep(5)
print(driver.title)
