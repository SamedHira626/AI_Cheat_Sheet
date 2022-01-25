from abc import ABC, abstractmethod  # abc is abstract base class
# We cannot create an object from Animal class (abstract class), this is the first rule of abstract class, any object cannot be created by abstract class
# We must use functions we used in superclass in the subclass 
class Animal(ABC): # super class                    
    
    @abstractmethod      # abstract method, child class'ta implement etmek zorunda olduğun methodlara denir
    def walk(self): pass

    def run(self): pass

class Bird(Animal): # sub class
    
    def __init__(self):
        print("bird")
        
    def walk(self): 
        print("walk")


b1 = Bird()
