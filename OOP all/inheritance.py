# parent
class Animal:
    a = 5
    __b = 6
    def __init__(self):
        print("animal is created")
    
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animal walk")
    
# child
class Monkey(Animal):
    def __init__(self):
        super().__init__() # use init of parent(animal) class
        Animal.__init__(self) # use init of parent(animal) class
        print(super().a)  # superclass's variable can be used with super()
        print("monkey is created")
    
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
    
    def fly(self):
        print("fly")        
#
m1 = Monkey()
print("----")
m1.toString()
m1.walk()
m1.climb()
print("----")
b1 = Bird()
b1.walk()
# b1.climb()
b1.fly()   
