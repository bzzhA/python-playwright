from base.base import Base
from pom.locators.register_page_locators import RegisterPageLocators
from data.data import Data
from playwright.sync_api import expect


class RegisterPage(Base):
    register_locators = RegisterPageLocators
    data = Data

    def entry_register_data_valid(self):
        self.page.locator(self.register_locators.REGISTER_FIRST_NAME).fill(self.data.name)
        self.page.locator(self.register_locators.REGISTER_EMAIL).fill(self.data.email)
        self.page.locator(self.register_locators.REGISTER_PASSWORD).fill(self.data.password)
        self.page.locator(self.register_locators.REGISTER_PHONE_NUMBER).fill(self.data.phone_number)
        self.page.locator(self.register_locators.REGISTER_CHECKBOX).click()
        self.page.get_by_text(self.register_locators.REGISTER_BUTTON).click()

    def entry_register_data_invalid(self):
        self.page.locator(self.register_locators.REGISTER_FIRST_NAME).fill(self.data.name)
        self.page.locator(self.register_locators.REGISTER_EMAIL).fill(self.data.email_invalid)
        self.page.locator(self.register_locators.REGISTER_PASSWORD).fill(self.data.password_invalid)
        self.page.locator(self.register_locators.REGISTER_PHONE_NUMBER).fill(self.data.phone_number)

    def check_register_invalid(self):
        expect(self.page.get_by_text(self.register_locators.CHECK_INVALID_PASSWORD)).to_be_visible()


