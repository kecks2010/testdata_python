from dataclasses import dataclass
from typing import Optional


@dataclass
class Payment:
    id: Optional[int]
    customer_id: int
    account_owner: str
    account_id: str
    payment_provider: str
    expiry_date: Optional[str]
    secure_code: Optional[str]
    payment_method: str