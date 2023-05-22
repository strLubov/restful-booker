from dataclasses import dataclass


@dataclass
class Room:
    name: str
    type: str
    accessible: str
    price: str

@dataclass
class Contact:
    name: str
    address: str
    phone: str
    email: str