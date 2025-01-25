from typing import  Optional

from testdata.model.customer.Address import Address
from testdata.service.testdata_repository.DatabaseConnection import DatabaseConnection


class AddressRepository:
    """
        This class provides methods to access the test data database and returns address objects.

        Author:
            Mirko Werner
    """
    def __init__(self, db_file: str):
        self.db_file = db_file

    def find_by_id(self, id: int) -> Optional[Address]:
        with DatabaseConnection(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM addresses WHERE id = ?
            """, (id,))
            row = cursor.fetchone()
            if row:
                address = self._map_address(row)
                return address

    @staticmethod
    def _map_address(row) -> Address:
        return Address(
            id=row["id"],
            street=row["street"],
            number=row["number"],
            postal_code=row["postal_code"],
            city=row["city"],
            state=row["state"],
            country=row["country"]
        )