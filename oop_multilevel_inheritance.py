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

class smartphone(android):
    def __init__(self, name, price, brand, os, ram, rom):
        super().__init__(name, price, brand, os)
        self.ram = ram
        self.rom = rom
    def show(self):
        super().show()
        print("RAM: ", self.ram)
        print("ROM: ", self.rom)            

sm1 = smartphone("A12", "Rs. 5000", "Samsung", "Android", "4GB", "64GB")
sm1.show()
sm2 = smartphone("iPhone 13", "Rs. 6000", "Apple", "iOS", "3GB", "32GB")
sm2.show()        

"""
Name:  A12      
Price:  Rs. 5000
Brand:  Samsung 
OS:  Android
RAM:  4GB
ROM:  64GB
Name:  iPhone 13
Price:  Rs. 6000
Brand:  Apple
OS:  iOS
RAM:  3GB
ROM:  32GB
"""
