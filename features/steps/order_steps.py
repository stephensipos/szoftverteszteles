
import json

from behave import given, when, then, step

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from locator import Locator
from locator import Wait

locators = {}
locators["empty_cart_warning"] = Locator(By.XPATH, "//div[@id='center_column']//p[contains(@class, 'warning') and (text() = 'Your shopping cart is empty.')]")
locators["cart_summary_head"] = Locator(By.XPATH, "//table[@id='cart_summary']/thead")
locators["cart_summary_body"] = Locator(By.XPATH, "//table[@id='cart_summary']/tbody")
locators["cart_summary_foot"] = Locator(By.XPATH, "//table[@id='cart_summary']/tfoot")

def add_product_to_cart(driver, url, id_product, qty=1):
    data = {
        "controller": "cart",
        "add": "1",
        "ajax": "true",
        "qty": f"{qty}",
        "id_product": f"{id_product}"
    }

    script = f"""
    $.ajax({{
        type: 'POST',
        url: '{url}',
        data: {json.dumps(data)},
        async: false
    }});
    """
    driver.execute_script(script)

@given("we are on the order page")
def step_impl(context):
  context.browser.get("http://automationpractice.com/index.php?controller=order")

@then(u'cart has no elements')
def step_impl(context):
  try:
    locators["cart_summary_body"].find_on(context.browser)
  except TimeoutException:
    assert True
    return
  
  assert False

@then(u'an empty cart warning is displayed')
def step_impl(context):
  empty_cart_warning = locators["empty_cart_warning"].find_on(context.browser)
  assert empty_cart_warning.is_displayed()

@given(u'an roder has been palced')
def step_impl(context):
  add_product_to_cart(context.browser, context.browser.current_url, 1, qty=1)


@when("we reload the page")
def step_impl(context):
  context.browser.refresh()


@then(u'no empty cart warning is displayed')
def step_impl(context):
  empty_cart_warning = locators["empty_cart_warning"].find_on(context.browser)
  assert not empty_cart_warning.is_displayed()