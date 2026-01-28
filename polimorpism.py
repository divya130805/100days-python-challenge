class home():
    def __init__(self,f_name,m_name,c_name):
        self.f_name=f_name
        self.m_name=m_name
        self.c_name=c_name

class data(home):
    def __init__(self,f_name,m_name,c_name,address):
        super().__init__(f_name,m_name,c_name)
        self.address=address
    def display(self):
        print(self.address,self.f_name,self.m_name,self.c_name)

data1=data('minjur','david','maria','leo')
data1.display()

#simple polimorphism
class dog():
    def sound(self):
        print("bow bowww")
class cat():
    def sound(self):
        print("meow meow")

animal=dog()
animal.sound()
ani=cat()
ani.sound()