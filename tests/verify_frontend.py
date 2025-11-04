
import re
from playwright.sync_api import Page, expect

def test_homepage_loads(page: Page):
    page.goto("http://localhost:8504")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Partiler Savaşı"))

    # Wait for the main header to be visible
    header = page.locator('h1').get_by_text('Partiler Savaşı')
    expect(header).to_be_visible()

    # Take a screenshot
    page.screenshot(path="frontend_verification.png")
