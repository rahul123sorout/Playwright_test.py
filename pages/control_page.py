from playwright.sync_api import Page


class ControlPage:

    def __init__(self, page: Page):
        self.page = page

        self.control_tab = page.get_by_role(
            "tab",
            name="Control"
        )

        self.red_color = page.locator(
            "css=div.qx-main-dark[style*='background-color:red']"
        )

        self.next_month_button = page.locator(
            "css=div[role='button'] div[style*='right.gif']"
        ).locator("..")

        self.date_one = page.locator(
            "xpath=//div[normalize-space(.)='1']"
        )

    def open_control(self):

        self.control_tab.click()

        self.page.wait_for_timeout(1500)

    def select_red(self):

        self.red_color.click()

        self.page.wait_for_timeout(1500)

    def select_next_month(self):

        self.next_month_button.click()

        self.page.wait_for_timeout(2000)

    def select_date_one(self):

        for i in range(self.date_one.count()):

            if self.date_one.nth(i).is_visible():

                self.date_one.nth(i).click()
                break

        self.page.wait_for_timeout(2000)