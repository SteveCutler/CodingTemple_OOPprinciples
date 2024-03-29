from productbase import Product

class Clothing(Product):
    def __init__(self, productID, name, price, season):
        super().__init__(productID, name, price)
        self.season = season

    def displayProduct(self):
        print(f"product: '{self.name}' is for {self.season} , has an ID of {self.productID}, and a price of ${self.price}!")
