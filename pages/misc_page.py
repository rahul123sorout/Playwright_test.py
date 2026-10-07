from playwright.sync_api import Page


class MiscPage:

    def __init__(self, page: Page):

        self.page = page

        self.misc_tab = page.get_by_role(
            "tab",
            name="Misc",
            exact=True
        )

        self.disabled_buttons = page.locator(
            "xpath=//div[@role='button' and "
            ".//div[normalize-space(.)='Disabled']]"
        )

        self.item_1_list = page.locator(
            "xpath=//div[normalize-space(.)='Item 1']"
        )

        self.right_drop_box = page.locator(
            'css=div[qxdroppable="on"][aria-orientation="vertical"]'
        )

    def open_misc(self):

        self.misc_tab.click()

        self.page.wait_for_timeout(1500)

    def click_disabled_button_twice(self):

        for i in range(self.disabled_buttons.count()):

            if self.disabled_buttons.nth(i).is_visible():

                disabled_button = self.disabled_buttons.nth(i)
                break

        disabled_button.click()
        self.page.wait_for_timeout(500)

        disabled_button.click()

        self.page.wait_for_timeout(1000)

    def drag_item_1(self):

        for i in range(self.item_1_list.count()):

            if self.item_1_list.nth(i).is_visible():

                item_1 = self.item_1_list.nth(i)
                break

        item_1.drag_to(self.right_drop_box)

        self.page.wait_for_timeout(2000)