from dataclasses import dataclass
from typing import Optional


@dataclass
class Payment:
    """
        Represents a payment entry for a customer.

        Author:
            Mirko Werner

        Attributes:
            id (int): id of the payment entry.
            customer_id (int): id of the connected customer.
            account_owner (str): name of the account owner.
            account_id (str): id of the account.
            payment_provider (str): name of the payment provider.
            expiry_date (str): expiry date of the payment entry.
            secure_code (str): secure code of the payment entry.
            payment_method (str): method of the payment (bank, paypal, creditcard, ...).
        """
    id: Optional[int]
    customer_id: int
    account_owner: str
    account_id: str
    payment_provider: str
    expiry_date: Optional[str]
    secure_code: Optional[str]
    payment_method: str