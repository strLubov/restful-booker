from faker import Faker
import pytest

from ui.data.model import Room
from ui.pages.admin_rooms_page import AdminRooms

fake = Faker()

@pytest.mark.parametrize("type", ["Single", "Double", "Twin", "Family", "Suite"])
def test_create_room(open_browser_with_cookie, type):
    room = Room(name='test_room', price="100", type=type, accessible="True")
    list_rooms = AdminRooms()
    list_rooms.create_room(room)

    # THEN

    list_rooms.open_created_room(room.name)
    list_rooms.check_room_name(room.name)
    list_rooms.check_room_price(room.price)


def test_update_room(open_browser_with_cookie):

    room_update = Room(name='room', price="100", type="Single", accessible="True")
    room_updated = Room(name='new_room', price="500", type="Twin", accessible="False")

    list_rooms = AdminRooms()

    list_rooms.create_room(room_update)

    list_rooms.open_created_room(room_update.name)

    list_rooms.edit(room_updated)

    # THEN

    list_rooms.check_room_name(room_updated.name)
    list_rooms.check_room_price(room_updated.price)
