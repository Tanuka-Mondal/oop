class mobile:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand
    def show(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Brand: ", self.brand)

class watch:
    def __init__(self, name, price, quality):
        self.name = name
        self.price = price
        self.quality = quality
    def show(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Quality: ", self.quality)

class smartwatch(mobile,watch):
    def __init__(self, name, price, quality, brand):
        self.name = name
        self.price = price
        self.quality = quality
        self.brand = brand
    def show(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Quality: ", self.quality)
        print("Brand: ", self.brand)

sw1 = smartwatch("A12", "Rs. 5000", "Very Good", "Samsung")   
sw1.show()     

"""
Name:  A12
Price:  Rs. 5000
Quality:  Very Good
Brand:  Samsung
"""
