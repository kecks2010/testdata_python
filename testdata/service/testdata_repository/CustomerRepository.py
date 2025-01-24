from datetime import datetime, timezone, timedelta
from typing import Optional

from dateutil.tz import tz

from testdata.model.customer.Address import Address
from testdata.model.customer.Customer import Customer
from testdata.model.customer.Login import Login
from testdata.model.customer.Payment import Payment
from testdata.service.testdata_repository.DatabaseConnection import DatabaseConnection


class CustomerRepository:
    def __init__(self, db_file: str):
        self.db_file = db_file

    def find_by_name(self, first_name: str, last_name: str) -> Optional[Customer]:
        if first_name is None or last_name is None:
            raise ValueError("first_name or last_name must not be none")
        with DatabaseConnection(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM customer WHERE first_name = ? AND last_name = ?
            """, (first_name, last_name))
            row = cursor.fetchone()
            if row:
                customer = self._map_customer(row)
                self._load_associated_data(customer, cursor)
                return customer
            return None

    def find_by_name_and_birthdate(self, first_name: str, last_name: str, birth_date: datetime) -> Optional[Customer]:
        if first_name is None or last_name is None or birth_date is None:
            raise ValueError("first_name, last_name or birthdate must not be none")
        birth_date = int(birth_date.timestamp()*1000)
        with DatabaseConnection(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM customer WHERE first_name = ? AND last_name = ? AND birth_date = ?
            """, (first_name, last_name, birth_date))
            row = cursor.fetchone()
            if row:
                customer = self._map_customer(row)
                self._load_associated_data(customer, cursor)
                return customer
            return None

    @staticmethod
    def _map_customer(row) -> Customer:
        death_date = None
        if row["death_date"] is not None:
            death_date = datetime.fromtimestamp(row["death_date"]/1000)
        return Customer(
            id=row["id"],
            gender=row["gender"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            birth_date=datetime.fromtimestamp(row["birth_date"]/1000),
            birth_place=row["birth_place"],
            death_date=death_date,
            death_place=row["death_place"],
            phone_number=row["phone_number"],
            mobile_number=row["mobile_number"],
            email_address=row["email_address"]
        )

    def _load_associated_data(self, customer: Customer, cursor):
        customer.addresses = self._find_addresses_by_customer_id(customer.id, cursor)
        customer.logins = self._find_logins_by_customer_id(customer.id, cursor)
        customer.payments = self._find_payments_by_customer_id(customer.id, cursor)

    @staticmethod
    def _find_addresses_by_customer_id(customer_id: int, cursor) -> list:
        cursor.execute("""
            SELECT addresses.*, customer_addresses.address_type FROM addresses addresses
            INNER JOIN customer_addresses customer_addresses ON addresses.id = customer_addresses.address_id
            WHERE customer_addresses.customer_id = ?
        """, (customer_id,))
        return [Address(**dict(row)) for row in cursor.fetchall()]

    @staticmethod
    def _find_logins_by_customer_id(customer_id: int, cursor) -> list:
        cursor.execute("""
            SELECT * FROM login WHERE customer_id = ?
        """, (customer_id,))
        return [Login(**dict(row)) for row in cursor.fetchall()]

    @staticmethod
    def _find_payments_by_customer_id(customer_id: int, cursor) -> list:
        cursor.execute("""
            SELECT * FROM payment WHERE customer_id = ?
        """, (customer_id,))
        return [Payment(**dict(row)) for row in cursor.fetchall()]
