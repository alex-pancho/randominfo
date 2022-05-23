import unittest
from rndinfo import *
from rndinfo.log import *


class GetRandomTests(unittest.TestCase):

    def test_99_create_person_success(self):
        import time
        """Success create class Person"""
        person = Person()
        self.assertIsInstance(person, Person)
        person_attr = person.get_details()
        self.assertIsInstance(person_attr, dict)
        self.assertIsInstance(person.first_name, str)
        self.assertIsInstance(person.last_name, str)
        self.assertIsInstance(person.full_name, str)
        self.assertIsInstance(person.birthdate, str)
        self.assertIsInstance(person.gender, str)
        self.assertIsInstance(person.email, str)
        self.assertIsInstance(person.login, str)
        for a, v in person_attr.items():
            if isinstance(v, dict):
                for a1, v1 in v.items():
                    log.debug(f"{a1}: {v1}")
            else:
                log.debug(f"{a}: {v}")
        log.debug("")

    def test_01_get_alpha(self):
        data = get_alfa()
        self.assertIsInstance(data, str)
        log.debug(data)

    def test_02_get_id(self):
        _id = get_id()
        self.assertIsInstance(int(_id), int)
        log.debug(_id)

    def test_03_get_first_name_none(self):
        name, gender = get_first_name()
        self.assertIsInstance(name, str)
        self.assertTrue(name[0].isupper())
        self.assertTrue(name[1].islower())
        log.debug([name, gender])

    def test_04_get_first_name_man(self):
        name, gender = get_first_name('male')
        self.assertIsInstance(name, str)
        self.assertTrue(name[0].isupper())
        self.assertTrue(name[1].islower())
        self.assertTrue('male' == gender)
        log.debug([name, gender])

    def test_05_get_first_name_w(self):
        name, gender = get_first_name('female')
        self.assertIsInstance(name, str)
        self.assertTrue(name[0].isupper())
        self.assertTrue(name[1].islower())
        self.assertTrue('female' == gender)
        log.debug([name, gender])

    def test_06_get_last_name(self):
        name = get_last_name()
        self.assertIsInstance(name, str)
        self.assertTrue(name[0].isupper())
        self.assertTrue(name[1].islower())
        log.debug(name)

    def test_07_get_gender(self):
        data = get_gender()
        self.assertTrue('male' in data)
        log.debug(data)

    def test_08_get_land(self):
        data = get_land()
        self.assertIsInstance(data, str)
        log.debug(data)

    def test_09_get_full_name(self):
        data = get_full_name()
        self.assertTrue(len(data) > 4)
        log.debug(data)

    def test_10_get_otp(self):
        data = get_otp()
        self.assertTrue(len(data) > 4)
        log.debug(data)

    def test_11_get_otp_digit(self):
        data = get_otp(alpha=False)
        self.assertTrue(isinstance(int(data), int))
        log.debug(data)

    def test_12_get_email(self):
        data = get_email()
        self.assertTrue(len(data) > 4)
        log.debug(data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
