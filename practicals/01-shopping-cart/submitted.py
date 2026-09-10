from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def clear_cart(self):
        self.products.clear()

    def total_items(self):
        return len(self.products)

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total


item1 = Product("Laptop", 45000)
item2 = Product("Desktop", 40000)

cart = Cart()
cart.add_product(item1)
cart.add_product(item2)

print(cart.total_price())

cart.remove_product(item1)
print(cart.total_price())
print(f"Total items: {cart.total_items()}")

cart.clear_cart()
