import os

import allure
import pytest
from dotenv import load_dotenv
from requests import Response
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api.helpers.api_client import BaseSession
from api.helpers.urls import endpoints
from ui.utils import attach


DEFAULT_BROWSER_VERSION = "100.0"


@pytest.fixture()
def api_ui_client():
    client = BaseSession(base_url="https://automationintesting.online/")
    return client


@pytest.fixture()
def login_admin_ui(api_ui_client):

    LOGIN_ADMIN = os.getenv('admin_login')
    PASSWORD_ADMIN = os.getenv('admin_password')

    payload = {
        'username': LOGIN_ADMIN,
        'password': PASSWORD_ADMIN
    }

    response: Response = api_ui_client.send_request(method='post', url=endpoints.LOGIN, json=payload,
                                                    allow_redirects=False)

    return api_ui_client


@pytest.fixture(scope="function")
def open_browser(setup_browser):
    browser.config.base_url = 'https://automationintesting.online/#/admin'


@pytest.fixture()
def open_browser_with_cookie(login_admin_ui, open_browser):
    with allure.step("Открываем браузер с предустановленными cookies"):
        token = login_admin_ui.cookies.get('token')

        browser.open("")
        browser.driver.add_cookie({"name": "token", "value": token})
        browser.open("")


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
