from dataclasses import dataclass
from typing import Optional


@dataclass
class Login:
    id: Optional[int]
    customer_id: int
    username: str
    password: str
    two_factor_id: Optional[str]
    two_factor_type: Optional[str]