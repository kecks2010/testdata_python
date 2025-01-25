from dataclasses import dataclass
from typing import Optional


@dataclass
class Login:
    """
        Represents a login entry for a customer.

        Author:
            Mirko Werner

        Attributes:
            id (int): id of the login entry.
            customer_id (int): id of the connected customer.
            username (str): username of the login entry.
            password (str): password of the login entry.
            two_factor_id (str): two-factor-id of the login entry.
            two-factor-type (str): two-factor-type of the login entry.
        """
    id: Optional[int]
    customer_id: int
    username: str
    password: str
    two_factor_id: Optional[str]
    two_factor_type: Optional[str]