import unittest

from testdata.service.testdata_repository.product_repository import ProductRepository


class TestProductRepository(unittest.TestCase):
    def test_get_count_of_all_entries(self):
        product_repository = ProductRepository()
        count = product_repository.get_count_of_all_entries()

        self.assertIsNotNone(count)
        self.assertEqual(count, 12)

    def test_get_product_for_id(self):
        product_repository = ProductRepository()
        product = product_repository.find_by_id(5)


        self.assertIsNotNone(product)
        self.assertEqual(product.product_id, 1205)
        self.assertEqual(product.product_name, "Basic Blue Jeans")
        self.assertEqual(product.price, "30.00")

    def test_get_product_for_id_not_exists(self):
        product_repository = ProductRepository()
        product = product_repository.find_by_id(0)


        self.assertIsNone(product)

    def test_get_product_for_product_id(self):
        product_repository = ProductRepository()
        product = product_repository.find_by_product_id(1205)


        self.assertIsNotNone(product)
        self.assertEqual(product.product_id, 1205)
        self.assertEqual(product.product_name, "Basic Blue Jeans")
        self.assertEqual(product.price, "30.00")

    def test_get_product_for_product_id_not_exist(self):
        product_repository = ProductRepository()
        product = product_repository.find_by_product_id(0)


        self.assertIsNone(product)

    def test_get_product_for_product_name(self):
        product_repository = ProductRepository()
        product = product_repository.find_by_product_name("Basic Blue Jeans")


        self.assertIsNotNone(product)
        self.assertEqual(product.product_id, 1205)
        self.assertEqual(product.product_name, "Basic Blue Jeans")
        self.assertEqual(product.price, "30.00")

    def test_get_product_for_product_name_not_exist(self):
        product_repository = ProductRepository()
        product = product_repository.find_by_product_name("Flupp")


        self.assertIsNone(product)
