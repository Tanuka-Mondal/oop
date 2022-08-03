class mobile:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand
    def show(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Brand: ", self.brand)

class android(mobile):
    def __init__(self, name, price, brand, os):
        super().__init__(name, price, brand)
        self.os = os
    def show(self):
        super().show()
        print("OS: ", self.os)

and1 = android("A12", "Rs. 5000", "Samsung", "Android")
and1.show()
and2 = android("iPhone 13", "Rs. 6000", "Apple", "iOS")
and2.show()                

"""
Name:  A12
Price:  Rs. 5000
Brand:  Samsung
OS:  Android
Name:  iPhone 13
Price:  Rs. 6000
Brand:  Apple
OS:  iOS
"""
