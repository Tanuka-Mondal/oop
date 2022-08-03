class pen:
    def __init__(self,colour,type): #parameterized constructor
        self.colour = colour
        self.type = type

    def show(self):
        print("Colour: ", self.colour)
        print("Type: ", self.type)

pen1 = pen("black","ballpoint")      
pen2 = pen("red","fountain")
pen3 = pen("blue","gel")  
pen1.show()
pen2.show()
pen3.show()

"""
Colour:  black
Type:  ballpoint
Colour:  red
Type:  fountain
Colour:  blue
Type:  gel
"""
