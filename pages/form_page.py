from playwright.sync_api import Page


class FormPage:

    def __init__(self, page: Page):
        self.page = page

        self.required_field = page.locator(
            'css=input[placeholder="required"]'
        )

        self.password_field = page.locator(
            "xpath=//input[@type='password' and @placeholder='password']"
        )

    def fill_required_field(self, value):
        self.required_field.fill(value)

    def fill_password(self, password):
        self.password_field.fill(password)