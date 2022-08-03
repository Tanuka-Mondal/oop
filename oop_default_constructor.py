class book:
    def __init__(self):
        self.title = "Physics book"
        self.author = "Ray and Martin"

    def show (self):
        print("Title: ", self.title)
        print("Author: ", self.author)   
        
physics = book()    
physics.show()

"""
Title:  Physics book
Author:  Ray and Martin
"""
