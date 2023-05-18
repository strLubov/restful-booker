from faker import Faker
from api.helpers.urls import endpoints
from requests import Response
from api.helpers.metods import check_ok_response
from api.models.booking import Booking
from api.shemas.booking import successful_booking, base_booking

fake = Faker()

def test_create_booking(booker_api_client):
    """Создание бронирования"""

    payload = Booking.booking_info()

    response: Response = booker_api_client.send_request(method='post', url=endpoints.BOOKING, json=payload)

    check_ok_response(response=response, schema=successful_booking)


def test_update_booking(booker_api_client, create_booking):
    """Обновление бронирования"""

    bookingid = create_booking
    headers = Booking.booking_headers()
    payload = Booking.booking_info()

    response: Response = booker_api_client.send_request(method='put', url=f'{endpoints.BOOKING}/{bookingid}', json=payload, headers=headers)

    check_ok_response(response=response, schema=base_booking)

    assert response.json().get('firstname', '') == payload.get('firstname')
    assert response.json().get('lastname', '') == payload.get('lastname')



def test_partial_update_booking(booker_api_client, create_booking):

    """Частичное обновление бронирования"""

    bookingid = create_booking

    headers = {'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='}

    payload = {'firstname': fake.first_name()}

    response: Response = booker_api_client.send_request(method='patch', url=f'{endpoints.BOOKING}/{bookingid}', json=payload, headers=headers)

    check_ok_response(response=response, schema=base_booking)

    assert response.json().get('firstname', '') == payload.get('firstname')


def test_delete_booking(booker_api_client, create_booking):

    """Удаление бронирования"""

    bookingid = create_booking

    headers = {'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='}

    response: Response = booker_api_client.send_request(method='patch', url=f'{endpoints.BOOKING}/{bookingid}', headers=headers)

    assert response.status_code == 200


