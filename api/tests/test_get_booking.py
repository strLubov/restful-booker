from allure import step
from requests import Response

from api.helpers.urls import Endpoints


def test_get_filter_by_name(booker_api_client, create_booking):
    """Get booking by name."""

    with step("Data preparation"):
        booking_id, booking_info = create_booking

        params = {
            'firstname': booking_info.get('firstname', ''),
            'lastname': booking_info.get('lastname', '')
        }

    with step("Send firstname change request"):
        response: Response = booker_api_client.send_request(method='get', url=Endpoints.BOOKING, params=params)

    with step("Check result"):
        result = next(
            (book.get('bookingid') for book in response.json() if book.get('bookingid') == booking_id), None)

        assert result is not None
        assert result == booking_id


def test_get_filter_by_id(booker_api_client, create_booking):
    """Get booking by id."""
    with step("Data preparation"):
        booking_id, booking_info = create_booking

    with step("Send firstname change request"):
        response: Response = booker_api_client.send_request(method='get', url=f'{Endpoints.BOOKING}/{booking_id}')

    with step("Check result"):
        assert response.json() == booking_info
