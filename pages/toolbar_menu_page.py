from playwright.sync_api import Page


class ToolbarMenuPage:

    def __init__(self, page: Page):
        self.page = page

        self.toolbar_tab = page.get_by_role(
            "tab",
            name="Toolbar/Menu"
        )

        self.toolbar_menu_button = page.locator(
            "xpath=//div[@role='button' and @aria-haspopup='menu']"
            "[.//div[normalize-space(.)='Toolbar MenuButton']]"
        )

        self.menu_radio_button = page.locator(
            "xpath=//div[normalize-space(.)='Menu RadioButton']"
        )

        self.menubar_button = page.locator(
            "xpath=//div[@role='button' and @aria-haspopup='menu']"
            "[.//div[normalize-space(.)='Menubar Button']]"
        ).first

        self.menu_checkbox = page.locator(
            "xpath=//div[normalize-space(.)='Menu MenuCheckBox']"
        )

    def open_toolbar_menu(self):

        self.toolbar_tab.click()

        self.page.wait_for_timeout(1500)

    def select_menu_radio_button(self):

        self.toolbar_menu_button.click()

        self.page.wait_for_timeout(1500)

        self.menu_radio_button.last.click()

        self.page.wait_for_timeout(1500)

    def select_menu_checkbox(self):

        self.menubar_button.click()

        self.page.wait_for_timeout(1500)

        self.menu_checkbox.last.click()

        self.page.wait_for_timeout(1500)