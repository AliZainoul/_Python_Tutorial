from collections import namedtuple
from typing import List, Union, Dict, Tuple

# Namedtuple for representing products
Product = namedtuple("Product", ["name", "price"])

class ShoppingCart:
    """
    A simple shopping cart class to manage products and calculate the total price.

    Attributes
    ----------
    items : list of Product
        A list of Product namedtuples currently in the shopping cart.

    Methods
    -------
    add_item(*args, **kwargs):
        Adds products to the cart. Supports multiple formats:
        - Product instances
        - dictionaries with 'name' and 'price' keys
        - tuples of (name, price)
        - keyword arguments with name=price
    calculate_total():
        Returns the total price of all items in the cart.
    """

    def __init__(self) -> None:
        """
        Initializes an empty shopping cart.
        """
        self.items: List[Product] = []

    def add_item(
        self,
        *args: Union[Product, Dict[str, Union[str, float]], Tuple[str, float]],
        **kwargs: float
    ) -> None:
        """
        Adds one or more products to the shopping cart.

        Parameters
        ----------
        *args : Product | dict | tuple
            Products to add. Each argument can be:
            - A Product instance
            - A dictionary with 'name' and 'price' keys
            - A tuple of (name, price)
        **kwargs : float
            Products passed as keyword arguments with the format name=price.

        Raises
        ------
        ValueError
            If an argument is not a recognized type or format.
        """
        for arg in args:
            if isinstance(arg, Product):
                self.items.append(arg)
            elif isinstance(arg, dict):
                product = Product(**arg)
                self.items.append(product)
            elif isinstance(arg, tuple) and len(arg) == 2:
                product = Product(*arg)
                self.items.append(product)
            else:
                raise ValueError(f"Invalid argument format: {arg!r}")

        for name, price in kwargs.items():
            self.items.append(Product(name, price))

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the cart.

        Returns
        -------
        float
            The sum of all product prices.
        """
        return sum(item.price for item in self.items)


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()

    # Adding items with different argument passing modes
    cart.add_item(Product("Laptop", 1000), Product("Phone", 500))
    cart.add_item({"name": "Headphones", "price": 100}, {"name": "Charger", "price": 50})
    cart.add_item(("Keyboard", 150), ("Mouse", 80))  # Using tuples
    cart.add_item(Monitor=300, Tablet=400)  # Using keyword arguments

    # Calculating the total and displaying it
    total = cart.calculate_total()
    print("Total amount in the shopping cart:", total)
