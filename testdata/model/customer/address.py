from enum import Enum

class AddressType(Enum):
    PRIMARY_ADDRESS = "primary"
    SECONDARY_ADDRESS = "secondary"
    PRE_ADDRESS = "pre"

from typing import Optional

from testdata.model.customer.enums.country import Country
from testdata.model.customer.enums.state import State

class Address(object):
    """
        Represents an address entry for a customer.

        Author:
            Mirko Werner

        Attributes:
            id (int): id of the address entry.
            street (str): street of the address.
            number (str): number of the address.
            postal_code (str): postal code of the address.
            city (str): city of the address.
            state (State): state of the address.
            country (Country): Country of the address.
            address_type (AddressType): type of the address.
        """
    def __init__(self, id: Optional[int], street: Optional[str], number: Optional[str], postal_code: str, city: str,
                 state: Optional[str], country: str, address_type: Optional[str] = None):
        self.id = id
        self.street = street
        self.number = number
        self.postal_code = postal_code
        self.city = city
        if state is not None:
            self.state = State.get_state_by_name(state)
        self.country = Country.get_country_by_name(country)
        if address_type is not None:
            self.address_type = AddressType(address_type)