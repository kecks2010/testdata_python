import unittest

from testdata.model.customer.enums.country import Country
from testdata.model.customer.enums.state import State
from testdata.service.testdata_repository.address_repository import AddressRepository


class TestAddressRepository(unittest.TestCase):

    def test_find_address_by_id(self):
        addresss_repository = AddressRepository()
        address = addresss_repository.find_by_id(1)


        self.assertIsNotNone(address)
        self.assertEqual(address.id, 1)
        self.assertEqual(address.street, "Karolinenpl.")
        self.assertEqual(address.number, "5")
        self.assertEqual(address.postal_code, "64289")
        self.assertEqual(address.city, "Darmstadt")
        self.assertEqual(address.state, State.DE_HE)
        self.assertEqual(address.country, Country.GERMANY)

    def test_find_address_by_id_not_exists(self):
        addresss_repository = AddressRepository()
        address = addresss_repository.find_by_id(0)


        self.assertIsNone(address)
