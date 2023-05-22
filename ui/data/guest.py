from dataclasses import dataclass


@dataclass
class Guest:
    first_name: str
    last_name: str
    email: str
    phone: str