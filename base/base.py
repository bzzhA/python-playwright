from playwright.sync_api import Page
class Base:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://lk-dev.og1.ru/new/auth?type=1"
        self.base_url_admin = "https://lms-dev.og1.ru/students-schedule"

    def open(self):
        self.page.goto(self.base_url)

    def open_admin(self):
        self.page.goto(self.base_url_admin)
