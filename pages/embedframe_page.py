from playwright.sync_api import Page


class EmbedFramePage:

    def __init__(self, page: Page):

        self.page = page

        self.embedframe_tab = page.get_by_role(
            "tab",
            name="EmbedFrame",
            exact=True
        )

        self.iframes = page.locator("css=iframe")

    def open_embedframe(self):

        self.embedframe_tab.click()

        self.page.wait_for_timeout(1500)

    def scroll_first_frame(self):

        first_frame = self.iframes.nth(0)

        first_frame.evaluate(
            "element => element.contentWindow.scrollTo("
            "0, element.contentDocument.body.scrollHeight)"
        )

        self.page.wait_for_timeout(1500)

    def scroll_themed_frame(self):

        themed_iframe = self.iframes.nth(1)

        themed_iframe.evaluate(
            "element => element.contentWindow.scrollTo("
            "0, element.contentDocument.body.scrollHeight)"
        )

        self.page.wait_for_timeout(2000)