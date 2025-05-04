# product.py

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price  # Getter method for price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value  # Setter method for price

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price  # Deleter method for price

# Example usage
p1 = Product(100)
print("Price:", p1.price)  # Using getter

p1.price = 200  # Using setter
print("Updated Price:", p1.price)

del p1.price  # Using deleter
