from faker import Faker

fake = Faker()


class CreateUser:

    @staticmethod
    def random(username: str):
        first_name = fake.first_name_male()
        lase_name = fake.last_name()
        email = fake.ascii_company_email()
        password = fake.password()
        phone = fake.phone_number()
        return {
            "id": 0,
            "username": username,
            "firstName": first_name,
            "lastName": lase_name,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": 0
        }
