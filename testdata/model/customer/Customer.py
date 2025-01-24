from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from testdata.model.customer.Address import Address, AddressType
from testdata.model.customer.Login import Login
from testdata.model.customer.Payment import Payment

@dataclass
class Customer:
    id: Optional[int]
    gender: Optional[str]
    first_name: str
    last_name: str
    birth_date: datetime
    birth_place: Optional[str]
    death_date: Optional[datetime]
    death_place: Optional[str]
    phone_number: Optional[str]
    mobile_number: Optional[str]
    email_address: str
    addresses: List[Address] = field(default_factory=list)
    logins: List[Login] = field(default_factory=list)
    payments: List[Payment] = field(default_factory=list)

    def get_primary_address(self) -> Optional[Address]:
        if self.addresses not in [None, []]:
            return next((address for address in self.addresses if address.address_type == AddressType.PRIMARY_ADDRESS),
                        None)

    def get_secondary_address(self) -> Optional[Address]:
        if self.addresses not in [None, []]:
            return next((address for address in self.addresses if address.address_type == AddressType.SECONDARY_ADDRESS),
                        None)

    def get_pre_addresses(self) -> Optional[List[Address]]:
        if self.addresses not in [None, []]:
            return next((address for address in self.addresses if address.address_type == AddressType.PRE_ADDRESS), None)