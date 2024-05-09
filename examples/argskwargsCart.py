from collections import namedtuple

Product = namedtuple("Product", ["name", "price"])

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, *args, **kwargs):
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
                raise ValueError("Invalid argument format")

        for name, price in kwargs.items():
            product = Product(name, price)
            self.items.append(product)

    def calculate_total(self):
        return sum(item.price for item in self.items)

cart = ShoppingCart()

# Adding items with different argument passing modes
cart.add_item(Product("Laptop", 1000), Product("Phone", 500))
cart.add_item({"name": "Headphones", "price": 100}, {"name": "Charger", "price": 50})
cart.add_item(("Keyboard", 150), ("Mouse", 80))  # Using tuples for the "Keyboard" and "Mouse" items

# Calculating the total and displaying it
total = cart.calculate_total()
print("Total amount in the shopping cart:", total)
