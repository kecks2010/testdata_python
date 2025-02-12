import os
from random import randrange
from typing import  Optional

from testdata.model.product.product import Product
from testdata.service.testdata_repository.database_connection import DatabaseConnection


class ProductRepository(DatabaseConnection):
    """
        This class provides methods to access the test data database and returns product objects.

        Author:
            Mirko Werner
    """
    def __init__(self):
        # self.db_file = os.path.abspath("../../../database/testdata.db")
        self.db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../database/testdata.db")

    def find_by_id(self, id: int) -> Optional[Product]:
        with DatabaseConnection(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM product WHERE id = ?
            """, (id,))
            row = cursor.fetchone()
            if row:
                product = self._map_product(row)
                return product

    def find_by_product_id(self, product_id: int) -> Optional[Product]:
        with DatabaseConnection(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM product WHERE product_id = ?
            """, (product_id,))
            row = cursor.fetchone()
            if row:
                product = self._map_product(row)
                return product

    def find_by_product_name(self, product_name: str) -> Optional[Product]:
        with DatabaseConnection(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM product WHERE product_name = ?
            """, (product_name,))
            row = cursor.fetchone()
            if row:
                product = self._map_product(row)
                return product

    def get_count_of_all_entries(self) -> Optional[int]:
        with DatabaseConnection(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT count(*) FROM product
            """)
            row = cursor.fetchone()
            if row:
                count = row["count(*)"]
                return count


    def get_random_product(self) -> Optional[Product]:
        count = self.get_count_of_all_entries()
        if count:
            random_product = randrange(count)
            return self.find_by_id(random_product)

    @staticmethod
    def _map_product(row) -> Product:
        return Product(
            id=row["id"],
            product_id=row["product_id"],
            product_name=row["product_name"],
            price=row["price"]
        )