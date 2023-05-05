from pom.pages.register_page import RegisterPage
from pom.pages.main_page import MainPage
from pom.pages.payment_page import PaymentPage

class TestPlatformChromium:
    def test_platform_register_positive_chromium(self, chromium_page):
        main_page = MainPage(chromium_page)
        register_page = RegisterPage(chromium_page)
        main_page.open()
        main_page.clck_on_register()
        register_page.entry_register_data_valid()

    def test_platform_register_negative_chromium(self, chromium_page):
        main_page = MainPage(chromium_page)
        register_page = RegisterPage(chromium_page)
        main_page.open()
        main_page.clck_on_register()
        register_page.entry_register_data_invalid()

        register_page.check_register_invalid(), "Check password invalid"

    def test_platform_sign_in_chromium(self, chromium_page):
        main_page = MainPage(chromium_page)
        payment_page = PaymentPage(chromium_page)
        main_page.open()
        main_page.sign_in_platform()

        payment_page.check_payment_page(), "Payment page doesn't open"



