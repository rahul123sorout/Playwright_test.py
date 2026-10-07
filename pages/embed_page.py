from playwright.sync_api import Page


class EmbedPage:

    def __init__(self, page: Page):

        self.page = page

        self.embed_tab = page.get_by_role(
            "tab",
            name="Embed",
            exact=True
        )

        self.html_scroll_box = page.locator(
            'css=div[tabindex="1"][qxselectable="on"]'
            '[style*="overflow-y:auto"]'
            '[style*="top:60px"]'
            '[style*="height:150px"]'
        ).first

    def open_embed(self):

        self.embed_tab.click()

        self.page.wait_for_timeout(1500)

    def scroll_html_to_bottom(self):

        self.html_scroll_box.evaluate(
            "element => element.scrollTop = element.scrollHeight"
        )

        self.page.wait_for_timeout(2000)