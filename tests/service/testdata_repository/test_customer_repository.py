from datetime import datetime
import unittest

from testdata.service.testdata_repository.customer_repository import CustomerRepository

class TestCustomerRepository(unittest.TestCase):
    def test_find_customer_by_first_name_and_last_name(self):
        customer_repository = CustomerRepository()
        customer = customer_repository.find_by_first_name_and_last_name("Harry", "Potter")

        self.assertIsNotNone(customer)
        self.assertEqual(customer.id, 1)
        self.assertEqual(customer.gender, "male")
        self.assertEqual(customer.first_name, "Harry")
        self.assertEqual(customer.last_name, "Potter")
        self.assertEqual(customer.birth_date, datetime(1980, 7, 31, 2))
        self.assertEqual(customer.birth_place, "Godric's Hollow")
        self.assertIsNone(customer.death_date)
        self.assertIsNone(customer.death_place)
        self.assertEqual(customer.phone_number, "+13225558531")
        self.assertEqual(customer.mobile_number, "+491731234567")
        self.assertEqual(customer.email_address, "harry.potter@mirko-werner.de")
        self.assertIsNotNone(customer.addresses)
        self.assertEqual(len(customer.addresses), 3)
        self.assertIsNotNone(customer.addresses[0].address_type)
        self.assertIsNotNone(customer.logins)
        self.assertEqual(len(customer.logins), 2)
        self.assertIsNotNone(customer.payments)
        self.assertEqual(len(customer.payments), 3)

    def test_find_customer_by_first_name_last_name_and_birth_date(self):
        customer_repository = CustomerRepository()
        birth_date = datetime(1980, 7, 31, 2)
        customer = customer_repository.find_by_name_and_birthdate("Harry", "Potter", birth_date)

        self.assertIsNotNone(customer)
        self.assertEqual(customer.id, 1)
        self.assertEqual(customer.gender, "male")
        self.assertEqual(customer.first_name, "Harry")
        self.assertEqual(customer.last_name, "Potter")
        self.assertEqual(customer.birth_date, datetime(1980, 7, 31, 2))
        self.assertEqual(customer.birth_place, "Godric's Hollow")
        self.assertIsNone(customer.death_date)
        self.assertIsNone(customer.death_place)
        self.assertEqual(customer.phone_number, "+13225558531")
        self.assertEqual(customer.mobile_number, "+491731234567")
        self.assertEqual(customer.email_address, "harry.potter@mirko-werner.de")
        self.assertIsNotNone(customer.addresses)
        self.assertEqual(len(customer.addresses), 3)
        self.assertIsNotNone(customer.addresses[0].address_type)
        self.assertIsNotNone(customer.logins)
        self.assertEqual(len(customer.logins), 2)
        self.assertIsNotNone(customer.payments)
        self.assertEqual(len(customer.payments), 3)

    def test_find_customer_by_first_name_and_last_name_not_exist(self):
        customer_repository = CustomerRepository()
        customer = customer_repository.find_by_first_name_and_last_name("Ginny", "Weasley")

        self.assertIsNone(customer)

    def test_find_customer_by_first_name_last_name_and_birth_date_not_exist(self):
        customer_repository = CustomerRepository()
        birth_date = datetime(1981, 7, 31, 2)
        customer = customer_repository.find_by_name_and_birthdate("Harry", "Potter", birth_date)

        self.assertIsNone(customer)
