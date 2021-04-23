
from time import sleep

from unittest import mock
import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from .base import Wait
from .base import Locator
from .base import driver
from .base import BaseTest

class TestAuthentication(BaseTest):
    start_location = "/index.php?controller=authentication"
    locators = {}
    locators["email"] = Locator(By.ID, "email")
    locators["passwd"] = Locator(By.ID, "passwd")
    locators["submit_login"] = Locator(By.ID, "SubmitLogin")
    locators["error"] = Locator(By.XPATH, "//div[contains(@class, 'alert-danger')]/ol/li[1]", Wait.MEDIUM)

    def test_email_input_has_no_error_class_by_default(self, driver):
        self.open_start_location(driver)

        email_input = self.locators["email"].find_on(driver)
        form_input = email_input.find_element_by_xpath('..')

        assert form_input.get_attribute("class").find("form-error") == -1


    @pytest.mark.parametrize("email", [
        (""),
        ("invalid email")
    ])
    def test_form_error_class_is_added_to_email_on_invalid_input(self, email, driver):
        self.open_start_location(driver)
        
        email_input = self.locators["email"].find_on(driver)
        email_input.send_keys(email)
        email_input.send_keys(Keys.TAB)

        form_input = email_input.find_element_by_xpath('..')

        assert form_input.get_attribute("class").find("form-error") != -1


    @pytest.mark.parametrize("email", [
        ("test@email.com")
    ])
    def test_form_ok_class_is_added_to_email_on_valid_input(self, email, driver):
        self.open_start_location(driver)
        
        email_input = self.locators["email"].find_on(driver)
        email_input.send_keys(email)
        email_input.send_keys(Keys.TAB)

        form_input = email_input.find_element_by_xpath('..')

        assert form_input.get_attribute("class").find("form-ok") != -1


    @pytest.mark.parametrize("email, passwd, error", [
        ("", "", "An email address required."),
        ("", "invalid password", "An email address required."),
        ("invalid email", "", "Invalid email address."),
        ("test@user.com", "", "Password is required."),
        ("test@user.com", "invalid password", "Authentication failed."),
    ])
    def test_invalid_login_results_in_error_message(self, email, passwd, error, driver):
        self.open_start_location(driver)

        self.locators["email"].find_on(driver).send_keys(email)
        self.locators["passwd"].find_on(driver).send_keys(passwd)
        self.locators["submit_login"].find_on(driver).click()

        assert self.locators["error"].find_on(driver).text == error

    # TODO: test for successful login
