import pytest
from requests import Response


from api.helpers.api_client import BaseSession
from api.helpers.urls import endpoints

from selene.support.shared import browser

from ui.data.booking import Booking

import allure


@pytest.fixture()
def api_ui_client():
    client = BaseSession(base_url="https://automationintesting.online/")
    return client


@pytest.fixture()
def login_admin_ui(api_ui_client):

    payload = {
        'username': 'admin',
        'password': 'password'
    }

    response: Response = api_ui_client.send_request(method='post', url=endpoints.LOGIN, json=payload, allow_redirects=False)

    return api_ui_client


@pytest.fixture(scope="function")
def open_browser():
    browser.config.base_url = 'https://automationintesting.online/#/admin'

    yield

    browser.quit()

@pytest.fixture()
def open_browser_with_cookie(login_admin_ui, open_browser):
    with allure.step("Открываем браузер с предустановленными cookies"):

        token = login_admin_ui.cookies.get('token')

        browser.open("")
        browser.driver.add_cookie({"name": "token", "value": token})
        browser.open("")



@pytest.fixture()
def create_booking(api_ui_client):
    payload = Booking.booking_info()

    response: Response = api_ui_client.send_request(method='post', url=endpoints.BOOKING, json=payload)

    return response