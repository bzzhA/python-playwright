# import pytest
# from playwright.sync_api import Playwright, BrowserType
#
#
# @pytest.fixture(scope='session')
# def driver_chromium(playwright: Playwright) -> BrowserType:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.set_viewport_size({"width": 1280, "height": 800})
#     yield page
#     page.close()
#
#
# @pytest.fixture(scope='session')
# def driver_firefox(playwright: Playwright) -> BrowserType:
#     browser = playwright.firefox.launch(headless=False)
#     page = browser.new_page()
#     page.set_viewport_size({"width": 1280, "height": 800})
#     yield page
#     page.close()
#
import pytest
from playwright.sync_api import Playwright, Browser, Page
@pytest.fixture(scope='session')
def chromium_browser(playwright: Playwright) -> Browser:
    browser = playwright.chromium.launch(headless=True, args=["--start-maximized"])
    yield browser
    browser.close()

@pytest.fixture(scope='session')
def firefox_browser(playwright: Playwright) -> Browser:
    browser = playwright.firefox.launch(headless=True, args=["--start-maximized"])
    yield browser
    browser.close()

@pytest.fixture(scope='session')
def chromium_page(chromium_browser: Browser) -> Page:
    page = chromium_browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope='session')
def firefox_page(firefox_browser: Browser) -> Page:
    page = firefox_browser.new_page()
    yield page
    page.close()
