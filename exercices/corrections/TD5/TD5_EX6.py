class Product:
    def __init__(self, name: str, price: float):
        if price <= 0.0:
            raise ValueError("Price cannot be negative")
        self._name = name
        self._price = price
    
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        if price <= 0.0:
            raise ValueError("Price cannot be negative")
        self._price = price

    def apply_discount(self, discount : float = 0.0):
        if discount < 0.0 or discount > 1.0:
            raise ValueError("Discount must be between 0.0 and 1.0")
        self._price *= (1-discount)
        return float(self._price)
    
    def __str__(self):
        return (f"Before our incredible 💵 discount 💵 this {self._name} costs {self._price} €\n"
                f"After our incredible 💵 discount 💵 this {self._name} costs {self.apply_discount()} € 😁😁😁")

product1 = Product("smartphone", 1120)
print(product1)
