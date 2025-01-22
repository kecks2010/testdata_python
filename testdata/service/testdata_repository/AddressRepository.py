import sqlite3
from typing import Dict, List, Optional

from testdata.model.customer.Address import Address


class AddressRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.index_by_id: Dict[int, Address] = {}
        self.index_by_customer_id: Dict[int, Address] = {}

        self._initialize_database()
        self._load_date()

    def _initialize_database(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS addresses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    street TEXT,
                    number TEXT,
                    postal_code TEXT,
                    city TEXT,
                    state TEXT,
                    country TEXT,
                    address_type TEXT,
                    customer_id INTEGER
                )
            """)
            conn.commit()

    def _load_date(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM addresses")
            rows = cursor.fetchall()

            for row in rows:
                address = Address(*row)
                self.index_by_id[address.id] = address
                if address.customer_id not in self.index_by_customer_id:
                    self.index_by_customer_id[address.customer_id] = []
                self.index_by_customer_id[address.customer_id].append(address)

