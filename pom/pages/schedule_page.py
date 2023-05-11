from base.base import Base
from pom.locators.schedule_page_locators import SchedulePageLocators
from data.data import Data
from playwright.sync_api import expect


class SchedulePage(Base):
    schedule_locators = SchedulePageLocators
    data = Data

    def entry_admin_data_valid(self):
        self.page.locator(self.schedule_locators.EMAIL).fill(self.data.admin_email)
        self.page.locator(self.schedule_locators.PASSWORD).fill(self.data.admin_password)
        self.page.get_by_text(self.schedule_locators.SIGN_IN_BUTTON).click()

    def entry_admin_data_invalid(self):
        self.page.locator(self.schedule_locators.EMAIL).fill(self.data.admin_email_invalid)
        self.page.locator(self.schedule_locators.PASSWORD).fill(self.data.admin_password_invalid)
        self.page.get_by_text(self.schedule_locators.SIGN_IN_BUTTON).click()
        expect(self.page.get_by_text(self.schedule_locators.INVALID_DATA)).to_be_visible()

    def select_filter(self):
        self.page.locator(self.schedule_locators.CALENDAR).click()
        self.page.locator(self.schedule_locators.YEAR).click()
        self.page.get_by_role("option", name="2023").get_by_text(self.schedule_locators.SELECT_YEAR).click()
        self.page.locator(self.schedule_locators.MONTH).click()
        self.page.get_by_role("option", name="апр.").get_by_text(self.schedule_locators.SELECT_MONTH).click()
        self.page.locator(self.schedule_locators.CALENDAR).click()
        self.page.get_by_role("row", name="03 04 05 06 07 08 09").get_by_text(self.schedule_locators.SELECT_DAY).click()
        self.page.locator(self.schedule_locators.FILTER).click()
        self.page.locator(self.schedule_locators.SELECT_CLASS_OPEN).click()
        self.page.locator(self.schedule_locators.SELECT_CLASS).click()
        self.page.get_by_text(self.schedule_locators.SHOW_RESULTS).click()
        expect(self.page.get_by_text(self.schedule_locators.TIME_LESSON).first).to_be_visible()
        expect(self.page.get_by_text(self.schedule_locators.TIME_LESSON).nth(1)).to_be_visible()
