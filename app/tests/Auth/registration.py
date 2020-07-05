from app.auth.functions import userRegister
import unittest

payload = {
    "name": "test",
    "email": "test@gmail.com",
    "password": "password",
    "type_of_user": "owner"
}


class RegistrationTest(unittest.TestCase):
    def test(self):
        self.assertFalse(userRegister(payload))


if __name__ == '__main__':
    unittest.main()
