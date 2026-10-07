from playwright.sync_api import Page


class TreePage:

    def __init__(self, page: Page):
        self.page = page

        self.tree_tab = page.get_by_role(
            "tab",
            name="Tree"
        )

        self.files_item = page.locator(
            "xpath=//div[normalize-space(.)='Files']"
        )

        self.sent_item = page.locator(
            "xpath=//span[normalize-space(.)='Sent']/ancestor::div[@role='gridcell']"
        )

    def open_tree(self):

        self.tree_tab.click()

        self.page.wait_for_timeout(1500)

    def select_files(self):

        self.files_item.first.click()

        self.page.wait_for_timeout(1500)

    def select_sent(self):

        self.sent_item.click()

        self.page.wait_for_timeout(1500)