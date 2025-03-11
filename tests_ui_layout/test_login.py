
from playwright.sync_api import Playwright, expect
import pytest

import utils.secret_config


@pytest.mark.parametrize("email", [
    "symonstorozhenko@gmail.com",
    pytest.param("fakeemail@example.com", marks=pytest.mark.xfail),
    pytest.param("jdsAIOJSDA@example.com", marks=pytest.mark.xfail)
])
@pytest.mark.parametrize("password", [
   utils.secret_config.PASSWORD,
    pytest.param("fakeemail", marks=pytest.mark.xfail),
    pytest.param("jdsajdsajdsaj", marks=pytest.mark.xfail)
])
def test_login(login_set_up, email, password) -> None:
    page = login_set_up
    page.goto("")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden(timeout=7000)
    all_links = page.get_by_role("link").all()
    for link in all_links:
        if '85$' in link.text_content():
            assert 'socks' not in link.text_content().lower() and 'notepad' not in link.text_content().lower()
    print("Yaya!")
    # ---------------------


