import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")
        sleep(2)
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("getting started with python")
        sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url
        sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
