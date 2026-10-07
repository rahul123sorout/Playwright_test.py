from playwright.sync_api import Page


class BasicPage:

    def __init__(self, page: Page):

        self.page = page

        self.basic_tab = page.get_by_role(
            "tab",
            name="Basic",
            exact=True
        )

        self.disabled_buttons = page.locator(
            "xpath=//div[@role='button' and "
            ".//div[normalize-space(.)='Disabled']]"
        )

    def open_basic(self):

        self.basic_tab.click()

        self.page.wait_for_timeout(1500)

    def click_disabled_button_three_times(self):

        for i in range(self.disabled_buttons.count()):

            if self.disabled_buttons.nth(i).is_visible():

                disabled_button = self.disabled_buttons.nth(i)
                break

        disabled_button.click()
        self.page.wait_for_timeout(500)

        disabled_button.click()
        self.page.wait_for_timeout(500)

        disabled_button.click()

        self.page.wait_for_timeout(1500)