from playwright.sync_api import Page


class ListPage:

    def __init__(self, page: Page):
        self.page = page

        self.list_tab = page.get_by_role(
            "tab",
            name="List"
        )

        self.binder_item = page.locator(
            "xpath=//div[normalize-space(.)='Binder, Marita']"
        )

        self.heiden_item = page.locator(
            "xpath=//div[normalize-space(.)='Heiden, Notfried']"
        )

    def open_list(self):

        self.list_tab.click()

        self.page.wait_for_timeout(1500)

    def select_binder(self):

        self.binder_item.last.click()

        self.page.wait_for_timeout(1500)

    def select_heiden(self):

        self.heiden_item.last.click()

        self.page.wait_for_timeout(1500)