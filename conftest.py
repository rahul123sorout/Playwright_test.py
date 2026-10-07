import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            channel="msedge",
            headless=False
        )

        page = browser.new_page()

        page.goto(
            "https://qooxdoo.org/qxl.widgetbrowser/",
            wait_until="domcontentloaded"
        )

        yield page

        browser.close()