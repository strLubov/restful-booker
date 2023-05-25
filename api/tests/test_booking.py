from allure import step
from faker import Faker
from requests import Response

from api.helpers.metods import check_ok_response
from api.helpers.urls import endpoints
from api.models.booking import Booking
from api.shemas.booking import successful_booking, base_booking

fake = Faker()


def test_create_booking(booker_api_client):
    """Create booking."""

    payload = Booking.booking_info()

    response: Response = booker_api_client.send_request(method='post', url=endpoints.BOOKING, json=payload)

    check_ok_response(response=response, schema=successful_booking)


def test_update_booking(booker_api_client, create_booking):
    """Update booking."""
    with step("Data preparation"):
        booking_id, _ = create_booking
        headers = Booking.booking_headers()
        payload = Booking.booking_info()

    with step("Send change request"):
        response: Response = booker_api_client.send_request(method='put', url=f'{endpoints.BOOKING}/{booking_id}',
                                                            json=payload, headers=headers)

    check_ok_response(response=response, schema=base_booking)

    with step("Check update"):
        assert response.json().get('firstname', '') == payload.get('firstname')
        assert response.json().get('lastname', '') == payload.get('lastname')


def test_partial_update_booking(booker_api_client, create_booking):
    """Partial update booking."""

    with step("Data preparation"):
        booking_id, _ = create_booking
        headers = Booking.booking_headers()
        payload = {'firstname': fake.first_name()}

    with step("Send firstname change request"):
        response: Response = booker_api_client.send_request(method='patch', url=f'{endpoints.BOOKING}/{booking_id}',
                                                            json=payload, headers=headers)

    with step("Check update"):
        check_ok_response(response=response, schema=base_booking)
        assert response.json().get('firstname', '') == payload.get('firstname')


def test_delete_booking(booker_api_client, create_booking):
    """Delete booking."""

    with step("Data preparation"):
        booking_id, _ = create_booking
        headers = Booking.booking_headers()

    with step("Send delete request"):
        response: Response = booker_api_client.send_request(method='delete', url=f'{endpoints.BOOKING}/{booking_id}',
                                                            headers=headers)

    with step("Check response"):
        assert response.status_code == 201
