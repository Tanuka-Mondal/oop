class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am an animal")
        
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)    

class bird:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print("I am a bird")

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Color:", self.color)  

tiger = animal("tiger", 10)
tiger.speak()
tiger.show()

crow = bird("crow", 2, "black")
crow.speak()
crow.show()


"""
I am an animal
Name: tiger
Age: 10
I am a bird
Name: crow
Age: 2
Color: black
"""
