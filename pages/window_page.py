from playwright.sync_api import Page


class WindowPage:

    def __init__(self, page: Page):
        self.page = page

        self.window_tab = page.get_by_role(
            "tab",
            name="Window"
        )

        self.show_close = page.locator(
            "xpath=//div[@role='checkbox' and "
            ".//div[normalize-space(.)='Show Close']]"
        )

        self.resize_frame = page.locator(
            "xpath=//div[@role='checkbox' and "
            ".//div[normalize-space(.)='Use resize frame']]"
        )

        self.modal_button_1 = page.locator(
            "xpath=//div[@role='button' and "
            ".//div[normalize-space(.)='Open Modal Dialog 1']]"
        )

        self.modal_checkbox = page.locator(
            "xpath=//div[@role='checkbox' and "
            ".//div[normalize-space(.)='Modal']]"
        )

    def open_window(self):

        self.window_tab.click()

        self.page.wait_for_timeout(1500)

    def uncheck_show_close(self):

        if self.show_close.get_attribute(
            "aria-checked"
        ) == "true":

            self.show_close.click()

        self.page.wait_for_timeout(1500)

    def uncheck_resize_frame(self):

        if self.resize_frame.get_attribute(
            "aria-checked"
        ) == "true":

            self.resize_frame.click()

        self.page.wait_for_timeout(1500)

    def open_modal_dialog(self):

        self.modal_button_1.click()

        self.page.wait_for_timeout(2000)

    def uncheck_modal(self):

        if self.modal_checkbox.get_attribute(
            "aria-checked"
        ) == "true":

            self.modal_checkbox.click()

        self.page.wait_for_timeout(2000)