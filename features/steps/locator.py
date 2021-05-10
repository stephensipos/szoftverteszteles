
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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