class Product:
    def __init__(self, productID, name, price):
        self.productID = productID
        self.name = name
        self.price = price

    def displayProduct(self):
        print(f"product: '{self.name}' has an ID of {self.productID} and a price of ${self.price}!")