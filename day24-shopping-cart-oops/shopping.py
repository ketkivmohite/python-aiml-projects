class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.__items = []  # Private attribute

    def add_item(self, product, quantity=1):
        self.__items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product_name):
        self.__items = [item for item in self.__items if item['product'].name != product_name]

    def calculate_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.__items)

    def get_items(self):
        # Return a copy to prevent direct modification
        return self.__items[:]

# Usage
cart = ShoppingCart()
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)
cart.add_item(p1, 1)
cart.add_item(p2, 2)

for item in cart.get_items():
    print(f"{item['product'].name} x {item['quantity']}")
print("Total:", cart.calculate_total())
