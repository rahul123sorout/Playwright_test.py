from playwright.sync_api import Page


class TablePage:

    def __init__(self, page: Page):
        self.page = page

        self.table_tab = page.get_by_role(
            "tab",
            name="Table"
        )

        self.id_cells = page.locator(
            "css=div[role='gridcell'][data-qx-table-cell-col='0']"
        )

        self.number_cells = page.locator(
            "css=div[role='gridcell'][data-qx-table-cell-col='1']"
        )

        self.number_header = page.locator(
            "xpath=//div[@role='columnheader']"
            "[.//div[normalize-space(.)='A number']]"
        )

    def open_table(self):

        self.table_tab.click()

        self.page.wait_for_timeout(1500)

    def select_id_cell(self):

        for i in range(self.id_cells.count()):

            if self.id_cells.nth(i).is_visible():

                self.id_cells.nth(i).click()
                break

        self.page.wait_for_timeout(1500)

    def select_number_cell(self):

        for i in range(self.number_cells.count()):

            if self.number_cells.nth(i).is_visible():

                self.number_cells.nth(i).click()
                break

        self.page.wait_for_timeout(1500)

    def click_number_header(self):

        self.number_header.click()

        self.page.wait_for_timeout(2000)