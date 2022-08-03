class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("I am an animal")
        
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

class wild_animal(animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("I am a wild animal")
        
    def show(self):
        super().show()
        print("Color:", self.color)   

class domestic_animal(animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("I am a domestic animal")
        
    def show(self):
        super().show()
        print("Color:", self.color)             
cow = animal("cow", 10)
cow.speak()
cow.show()

lion = wild_animal("lion", 10, "yellow")
lion.speak()
lion.show()    

dog = domestic_animal("dog", 2, "black")
dog.speak()
dog.show()

"""
I am an animal
Name: cow
Age: 10
I am a wild animal
Name: lion
Age: 10
Color: yellow
I am a domestic animal
Name: dog
Age: 2
Color: black
"""
