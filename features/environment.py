from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def selenium_browser(context):
    context.browser = webdriver.Firefox()
    yield context.browser
    context.browser.quit()

def before_scenario(context, scenario):
  use_fixture(selenium_browser, context)