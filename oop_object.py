class mobile:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand
    def show(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Brand: ", self.brand)

mob1 = mobile("A12", "Rs. 5000", "Samsung")    
mob1.show()
mob2 = mobile("iPhone 13", "Rs. 6000", "Apple")
mob2.show()
