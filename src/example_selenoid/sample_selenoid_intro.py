from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "version": "84.0",
    "enableVNC": True,
    "enableVideo": False
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

try:
    print('Session ID is: %s' % driver.session_id)
    print('Opening the page...')
    driver.get('https://www.lohika.com.ua/')

    print('Taking screenshot...')
    driver.get_screenshot_as_file(driver.session_id + '.png')
finally:
    driver.quit()
