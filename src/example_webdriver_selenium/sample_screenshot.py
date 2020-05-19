import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://www.python.org/')
driver.maximize_window()
driver.save_screenshot('python.png')
time.sleep(15)
driver.quit()
