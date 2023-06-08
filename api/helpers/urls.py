from enum import Enum


class Endpoints(str, Enum):
    BOOKING = 'booking'
    AUTH = 'auth'
    LOGIN = 'auth/login'
    ROOMS = 'room'

    def __str__(self) -> str:
        return self.value
