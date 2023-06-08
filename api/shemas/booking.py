from voluptuous import Schema, PREVENT_EXTRA

successful_booking = Schema(
    {
        "bookingid": int,
        "booking":
            {
                "firstname": str,
                "lastname": str,
                "totalprice": int,
                "depositpaid": bool,
                "bookingdates":
                {
                    "checkin": str,
                    "checkout": str
                },
                "additionalneeds": str
               }
    },
    extra=PREVENT_EXTRA,
    required=True
)

base_booking = Schema(
    {
            "firstname": str,
            "lastname": str,
            "totalprice": int,
            "depositpaid": bool,
            "bookingdates":
            {
                "checkin": str,
                "checkout": str
            },
            "additionalneeds": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

booking = Schema(
    {
        "bookingid": int,
        "booking":
            base_booking,
    },
    extra=PREVENT_EXTRA,
    required=True
)
