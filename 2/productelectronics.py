from productbase import Product

class Electronics(Product):
    def __init__(self, productID, name, price, category):
        super().__init__(productID, name, price)
        self.category = category

    def displayProduct(self):
        print(f"product: '{self.name}' is in the {self.category} electronics category, has an ID of {self.productID}, and a price of ${self.price}!")
