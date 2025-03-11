from playwright.sync_api import Playwright, expect
from pom.home_page_elements import HomePage
import pytest

def test_about_us_section_verbiage(login_set_up):
    page = login_set_up
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()


@pytest.mark.xfail(reason="celebrate_header is visible")
def test_about_us_section_verbiage_2(login_set_up):
    page = login_set_up
    home_page = HomePage(page)

    expect(home_page.celebrate_header).not_to_be_visible()