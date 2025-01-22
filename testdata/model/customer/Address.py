from typing import Optional
from dataclasses import dataclass

@dataclass
class Address:
    id: Optional[int]
    street: Optional[str]
    number: Optional[str]
    postal_code: str
    city: str
    state: Optional[str]
    country: str