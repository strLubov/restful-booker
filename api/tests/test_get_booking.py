from api.helpers.urls import endpoints
from requests import Response


def test_get_filter_by_name(booker_api_client, create_booking):

    booking_id, booking_info = create_booking

    params = {
        'firstname': booking_info.get('firstname', ''),
        'lastname': booking_info.get('lastname', '')
    }

    response: Response = booker_api_client.send_request(method='get', url=endpoints.BOOKING, params=params)

    result = next(
        (book.get('bookingid') for book in response.json() if book.get('bookingid') == booking_id), None)

    assert result is not None
    assert result == booking_id

def test_get_filter_by_id(booker_api_client, create_booking):

    booking_id, booking_info = create_booking

    response: Response = booker_api_client.send_request(method='get', url=f'{endpoints.BOOKING}/{booking_id}')

    assert response.json() == booking_info





