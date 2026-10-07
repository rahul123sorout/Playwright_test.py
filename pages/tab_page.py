from playwright.sync_api import Page


class TabPage:

    def __init__(self, page: Page):
        self.page = page

        self.tab_section = page.get_by_role(
            "tab",
            name="Tab",
            exact=True
        )

        self.notes_tabs = page.locator(
            "xpath=//div[@role='tab' and "
            ".//div[normalize-space(.)='Notes']]"
        )

        self.calculator_tabs = page.locator(
            "xpath=//div[@role='tab' and "
            ".//div[normalize-space(.)='Calculator']]"
        )

    def open_tab_section(self):

        self.tab_section.click()

        self.page.wait_for_timeout(1500)

    def select_notes(self):

        self.notes_tabs.nth(0).click()

        self.page.wait_for_timeout(1500)

    def select_calculator(self):

        self.calculator_tabs.nth(1).click()

        self.page.wait_for_timeout(1500)