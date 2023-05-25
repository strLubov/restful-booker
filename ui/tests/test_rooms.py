import time

from ui.data.model import Room
from ui.pages.admin_rooms_page import AdminRooms


room = Room(name="test_room", price="100", type = "Double", accessible="True")

room_update = Room(name="test_room_new", price="500", type = "Twin", accessible="False")


def test_create_room(open_browser_with_cookie):

    list_rooms = AdminRooms()
    list_rooms.create_room(room)

    #THEN

    list_rooms.open_created_room(room.name)
    list_rooms.check_room_name(room.name)
    list_rooms.check_room_price(room.price)




def test_update_room(open_browser_with_cookie):
    list_rooms = AdminRooms()

    list_rooms.create_room(room)

    list_rooms.open_created_room(room.name)

    list_rooms.edit(room_update)

    #THEN

    list_rooms.check_room_name(room_update.name)
    list_rooms.check_room_price(room_update.price)


