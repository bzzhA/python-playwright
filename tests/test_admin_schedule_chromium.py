from pom.pages.schedule_page import SchedulePage


class TestAdminScheduleChromium:

    def test_admin_sign_in_invalid(self, chromium_page):
        schedule_page = SchedulePage(chromium_page)
        schedule_page.open_admin()
        schedule_page.entry_admin_data_invalid()

    def test_admin_sign_in_valid(self, chromium_page):
        schedule_page = SchedulePage(chromium_page)
        schedule_page.entry_admin_data_valid()

    def test_filter_admin(self, chromium_page):
        schedule_page = SchedulePage(chromium_page)
        schedule_page.select_filter()
