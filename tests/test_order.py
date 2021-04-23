
from time import sleep
from time import time

from unittest import mock
import pytest
import requests

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from .base import Wait
from .base import Locator
from .base import driver
from .base import BaseTest

def add_product_to_cart(driver, url, id_product, qty=1):
    data = {
        "controller": "cart",
        "add": "1",
        "ajax": "true",
        "qty": f"{qty}",
        "id_product": f"{id_product}"
    }

    driver.request("POST", url, data=data)

    # cookies = driver.get_cookies()
    # session = requests.Session()
    # for cookie in cookies:
    #     session.cookies.set(cookie['name'], cookie['value'], domain=cookie["domain"], path=cookie["path"])
    # response = session.post(url, data=data)

class TestAuthentication(BaseTest):
    start_location = "/index.php?controller=order"

    locators = {}
    # locators["center_column"] = Locator(By.ID, "center_column")
    locators["empty_cart_warning"] = Locator(By.XPATH, "//div[@id='center_column']//p[contains(@class, 'warning') and (text() = 'Your shopping cart is empty.')]")
    locators["cart_summary_head"] = Locator(By.XPATH, "//table[@id='cart_summary']/thead")
    locators["cart_summary_body"] = Locator(By.XPATH, "//table[@id='cart_summary']/tbody")
    locators["cart_summary_foot"] = Locator(By.XPATH, "//table[@id='cart_summary']/tfoot")

    def test_caret_is_empty_by_default(self, driver):
        self.open_start_location(driver)

        try:
            empty_cart_warning = self.locators["cart_summary_body"].find_on(driver)
        except TimeoutException:
            assert True
            return
        
        assert False

    def test_no_item_in_caret_no_empty_caret_warning_is_displayed(self, driver):
        self.open_start_location(driver)

        empty_cart_warning = self.locators["empty_cart_warning"].find_on(driver)

        assert empty_cart_warning.is_displayed()

    def test_one_item_in_caret_no_empty_caret_warning_is_not_displayed(self, driver):
        driver.get(self.host)
        add_product_to_cart(driver, driver.current_url, 1, qty=1)
        self.open_start_location(driver)
        
        empty_cart_warning = self.locators["empty_cart_warning"].find_on(driver)

        assert not empty_cart_warning.is_displayed()
