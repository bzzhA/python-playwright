from base.base import Base
from pom.locators.payment_page_locators import PaymentPageLocators
from data.data import Data
from playwright.sync_api import expect


class PaymentPage(Base):

    payment_locators = PaymentPageLocators
    data = Data

    def check_payment_page(self):
        expect(self.page.locator(self.payment_locators.CHECK_RATE)).to_have_text('Доступ к материалам тарифа «Любознательный»')
