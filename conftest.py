import os

import pytest
from playwright.sync_api import Playwright

from utils.secret_config import PASSWORD

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD

@pytest.fixture(scope="function")
def set_up(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symontorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    yield page
    page.close()

@pytest.fixture(scope="function")
def login_set_up(set_up):
    page = set_up
    page.set_default_timeout(15000)
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(PASSWORD, timeout=3000)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    yield page