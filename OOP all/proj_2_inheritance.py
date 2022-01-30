class W():
      def __init__(self, name, surname):
            self.name = name
            self.surname = surname
            print("first constructor")           

class Website(W):
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def loginInfo(self):
        print(self.name + " " + self.surname )

class Website1(Website):
    "child"
    def __init__(self, name, surname, ids):
        #W.__init__(self, name, surname)  # you can use superclass's superclass's constructor
        Website.__init__(self, name, surname) 
        self.ids = ids
    
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)
class Website2(Website):

    def __init__ (self, name, surname, email):
        Website.__init__(self,name,surname)
        self.email = email

    def login(self):
        print(self.name + " " + self.surname + " " + self.email)
          
p1 = Website("name","surname")
p2 = Website1("name","surname", "123")
p3 = Website2("name","surname", "email@")

p1.loginInfo()
print("---")
p2.login()
p2.loginInfo()
# p2.name
# p2.surname
