from base.base import Base
from pom.locators.main_page_locators import MainPageLocators
from data.data import Data


class MainPage(Base):
    main_locators = MainPageLocators
    data = Data

    def clck_on_register(self):
        self.page.get_by_text(self.main_locators.REGISTER_BUTTON).click()

    def sign_in_platform(self):
        self.page.locator(self.main_locators.EMAIL).fill(self.data.email)
        self.page.locator(self.main_locators.PASSWORD).fill(self.data.password)
        self.page.get_by_text(self.main_locators.SIGN_IN_BUTTON).click()
