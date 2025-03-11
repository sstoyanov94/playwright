
from pom.contact_us_page import ContactUsPage
import pytest

def test_submit_form(set_up):
    page = set_up
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Svetoslav", "123 ulica", "test@email.com", "123-432-5354", "test subject", "test message")


