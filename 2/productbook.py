
from productbase import Product

class Book(Product):
    def __init__(self, productID, name, price, author):
        super().__init__(productID, name, price)
        self.author = author

    def displayProduct(self):
        print(f"product: '{self.name}' was written by {self.author}, has an ID of {self.productID}, and a price of ${self.price}!")
