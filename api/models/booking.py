from faker import Faker

fake = Faker()


class Booking:
    @staticmethod
    def booking_info():
        firstname = fake.first_name()
        lastname = fake.last_name()
        totalprice = fake.random_int(min=100, max=900)
        depositpaid = fake.boolean()
        checkin = fake.date()
        checkout = fake.date()
        additionalneeds = fake.bothify()

        return {
            'firstname': firstname,
            'lastname': lastname,
            'totalprice': totalprice,
            'depositpaid': depositpaid,
            'bookingdates':
                {
                    'checkin': checkin,
                    'checkout': checkout
                },
            'additionalneeds': additionalneeds}

    @staticmethod
    def booking_headers():
        authorization = 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        # тестовая площадка, генереция токена не работает поэтому он захардкожен

        return {
                'Authorization': authorization}
