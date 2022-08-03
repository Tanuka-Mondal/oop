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

class smartphone(mobile):
    def __init__(self, name, price, brand, os, ram):
        super().__init__(name, price, brand)
        self.os = os
        self.ram = ram
    def show(self):
        super().show()
        print("OS: ", self.os)
        print("RAM: ", self.ram)

mob1 = android("A12", "Rs. 5000", "Samsung", "Android 10")
mob1.show()
mob2 = smartphone("iPhone 13", "Rs. 6000", "Apple", "iOS 13", "4GB")
mob2.show()
        
"""
Name:  A12
Price:  Rs. 5000
Brand:  Samsung
OS:  Android 10
Name:  iPhone 13
Price:  Rs. 6000
Brand:  Apple
OS:  iOS 13
RAM:  4GB
"""  
