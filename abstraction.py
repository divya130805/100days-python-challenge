from abc import ABC,abstractmethod
class phone(ABC):
    @abstractmethod
    def price(self):
        pass
    @abstractmethod
    def ram(self):
        pass
    @abstractmethod
    def gb(self):
        pass
    @abstractmethod      # this is a abstract method it is not they means it is normal method ,if we take this decorator we can access with a below functiondeclaraction this could be call in the class redmi,oppo then only it will print or else error
    def colour(self):
        pass

class redmi(phone):
    def price(self):
        print(20000)
    def ram(self):
        print(200)
    def gb(self):
        print(512)
    def colour(self):
        print("blue")
    
class oppo(phone):
    def price(self):
        print(30000)
    def ram(self):
        print(220)
    def gb(self):
        print(220)
    def colour(self):
        print("white")


p1=redmi()
p1.price()
p1.ram()
p1.gb()
p1.colour()
p2=oppo()
p2.price()
p2.ram()
p2.gb()
p2.colour()


   