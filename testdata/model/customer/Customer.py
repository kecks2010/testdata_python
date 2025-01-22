from dataclasses import dataclass, field
from typing import Optional, List

from testdata.model.customer.Address import Address
from testdata.model.customer.Login import Login
from testdata.model.customer.Payment import Payment


@dataclass
class Customer:
    id: Optional[int]
    gender: Optional[str]
    first_name: str
    last_name: str
    birth_date: str
    birth_place: Optional[str]
    death_date: Optional[str]
    death_place: Optional[str]
    phone_number: Optional[str]
    mobile_number: Optional[str]
    email_address: str
    addresses: List[Address] = field(default_factory=list)
    logins: List[Login] = field(default_factory=list)
    payments: List[Payment] = field(default_factory=list)
