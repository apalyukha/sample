from time import sleep

from selenium.webdriver import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://demo.guru99.com/test/drag_drop.html")

sleep(3)

source_element = driver.find_element_by_xpath("//*[@id='credit2']/a")
dest_element = driver.find_element_by_xpath("//*[@id='bank']/li")
ActionChains(driver).drag_and_drop(source_element, dest_element).perform()

sleep(3)

driver.quit()
