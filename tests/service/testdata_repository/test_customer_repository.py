import unittest

from testdata.service.testdata_repository.CustomerRepository import CustomerRepository

class MyTestCase(unittest.TestCase):
    def test_something(self):

        repo = CustomerRepository("../../../database/testdata.db")
        customer = repo.find_by_name("Harry", "Potter")

        if customer:
            print("Kunde gefunden:", customer)
            print("Adressen:", customer.addresses)
            print("Logins:", customer.logins)
            print("Zahlungen:", customer.payments)
        else:
            print("Kunde nicht gefunden.")


if __name__ == '__main__':
    unittest.main()
