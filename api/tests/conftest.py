import pytest
from allure import step
from requests import Response

from api.helpers.api_client import BaseSession
from api.helpers.metods import check_ok_response
from api.helpers.urls import endpoints
from api.models.booking import Booking
from api.shemas.booking import successful_booking


@pytest.fixture()
def booker_api_client():
    client = BaseSession(base_url="https://restful-booker.herokuapp.com/")
    return client

@pytest.fixture()
def create_booking(booker_api_client):
    with step("Предварительное создание бронирования"):

        payload = Booking.booking_info()
        response: Response = booker_api_client.send_request(method='post', url=endpoints.BOOKING, json=payload)

        result = check_ok_response(response=response, schema=successful_booking)

        id = result["bookingid"]

        return id, result.get("booking")
