import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class MyScreenshot(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_takescreenshot(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://wallpaperscraft.com/')

        driver.save_screenshot('wallpaper.png')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
