class BankAccount(object):
    
    __bankId = 0  
    
    def __init__(self, name, money, address):
        self.name = name  # global
        self.__money = money  # private
        self.address = address
        
    # get and set global
    def getMoney(self):         
        return str(self.__money) + " " + str(self.__bankId) 
  
    def getMoney2(self):         
        return self.__money , self.__bankId
    
    def setMoney(self, amount):
        self.__bankId = 1  
        self.__money = amount
        
    # private
    def __increase(self):
        self.__money = self.__money + 500
        
#
p1 = BankAccount("messi", 1000, "barcelona")
p2 = BankAccount("neymar", 2000, "paris")


print("get method:",p1.getMoney())
# print("get method:",p1.__money)
p1.setMoney(5000)
print("after set method:",p1.getMoney())
a, b = p1.getMoney2()
print("money = {} id = {}".format(a,b))

# p1.__increase()
#print("after raise: ",p1.getMoney())
