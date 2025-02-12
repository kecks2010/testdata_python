class Product(object):
    """
        Represents a product entry.

        Author:
            Mirko Werner

        Attributes:
            id (int): id of the product entry.
            product_id (int): id of the product.
            product_name (str): name of the product.
            price (str): price of the product.
        """
    def __init__(self, id: int, product_id: int, product_name: str, price: str):
        self.id = id
        self.product_id = product_id
        self.product_name = product_name
        self.price = price