from seleniumrequests import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class Wait():
    SHORT = 1
    MEDIUM = 5
    LONG = 30

class Locator():
    by = None
    value = None
    wait = None

    def __init__(self, by, value, wait = Wait.SHORT):
        self.by = by
        self.value = value
        self.wait = wait

    def find_on(self, root):
        wait = WebDriverWait(root, self.wait)
        return wait.until(EC.presence_of_element_located((self.by, self.value)))

@pytest.fixture
def driver():
    driver = Firefox()
    yield driver
    #driver.quit()

class BaseTest():
    host = "http://automationpractice.com"
    start_location = "/"

    def open_start_location(self, driver):
        driver.get(self.host + self.start_location)
