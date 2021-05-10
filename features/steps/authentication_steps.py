from behave import given, when, then, step

from behave import register_type, use_step_matcher
import parse

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from locator import Locator
from locator import Wait

locators = {}
locators["email"] = Locator(By.XPATH, "//.[@name='email']")
locators["email_field"] = Locator(By.XPATH, "//.[@name='email']/..")
locators["passwd"] = Locator(By.ID, "passwd")
locators["submit_login"] = Locator(By.ID, "SubmitLogin")
locators["error"] = Locator(By.XPATH, "//div[contains(@class, 'alert-danger')]/ol/li[1]", Wait.MEDIUM)

@parse.with_pattern(r".*")
def parse_string(text):
  return text.strip()

register_type(Email=parse_string)
register_type(Password=parse_string)
use_step_matcher("cfparse")

@given("we are on the login page")
def step_impl(context):
  context.browser.get("http://automationpractice.com/index.php?controller=authentication")


@then(u'the email field has no error class')
def step_impl(context):
  form_input = locators["email_field"].find_on(context.browser)
  assert form_input.get_attribute("class").find("form-error") == -1


@given(u'an email as "{email:Email?}"')
def step_impl(context, email):
  context.email = email or ""


@given(u'a password as "{password:Password?}"')
def step_impl(context, password):
  context.password = password or ""


@given(u'an error message as "{error_message}"')
def step_impl(context, error_message):
  context.error_message = error_message or ""


@when(u'we set the email')
def step_impl(context):
  email_input = locators["email"].find_on(context.browser)
  email_input.send_keys(context.email)
  email_input.send_keys(Keys.TAB)

@then(u'the email field gets an error class')
def step_impl(context):
  form_input = locators["email_field"].find_on(context.browser)
  assert form_input.get_attribute("class").find("form-error") != -1


@then(u'the email field gets an ok class')
def step_impl(context):
  form_input = locators["email_field"].find_on(context.browser)
  assert form_input.get_attribute("class").find("form-ok") != -1


@given(u'a set of invalid credential values')
def step_impl(context):
  #raise NotImplementedError(u'STEP: Given a set of invalid credential values')
  pass


@when(u'we set the credentials')
def step_impl(context):
  email_input = locators["email"].find_on(context.browser)
  email_input.send_keys(context.email)
  email_input.send_keys(Keys.TAB)

  password_input = locators["passwd"].find_on(context.browser)
  password_input.send_keys(context.password)
  password_input.send_keys(Keys.TAB)

@when(u'click the Login button')
def step_impl(context):
  locators["submit_login"].find_on(context.browser).click()


@then(u'the expected error message is shown')
def step_impl(context):
  assert locators["error"].find_on(context.browser).text == context.error_message