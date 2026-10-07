from playwright.sync_api import Page


class ComboPage:

    def __init__(self, page: Page):
        self.page = page

        # Normal ComboBox
        self.normal_combo = page.locator(
            'css=div[role="combobox"][tabindex="4"]'
        )

        self.normal_combo_button = self.normal_combo.locator(
            'css=div[role="button"]'
        )

        self.item_9 = page.locator(
            "xpath=//div[@role='option' and normalize-space(.)='Item 9']"
        )

        # Virtual ComboBox
        self.virtual_combo = page.locator(
            'css=div[tabindex="5"]'
        )

        self.virtual_combo_button = self.virtual_combo.locator(
            'css=div[role="button"]'
        )

        self.item_299 = page.locator(
            "xpath=//div[normalize-space(.)='Item 299' "
            "and not(contains(@style,'visibility: hidden'))]"
        )

        self.virtual_input = self.virtual_combo.locator(
            'css=input[placeholder="Pick an item"]'
        )

    def select_item_9(self):

        self.normal_combo_button.click()

        self.item_9.click()

    def select_item_299(self):

        self.virtual_combo_button.click()

        self.virtual_combo.hover()

        for _ in range(300):

            if (
                self.item_299.count() > 0
                and self.item_299.last.is_visible()
            ):
                self.item_299.last.click()
                return

            self.page.mouse.wheel(0, 1000)
            self.page.wait_for_timeout(60)

        raise Exception(
            "Item 299 could not be reached in VirtualComboBox"
        )

    def get_selected_virtual_item(self):

        return self.virtual_input.input_value()