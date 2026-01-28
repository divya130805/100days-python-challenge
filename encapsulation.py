class company():
    def __init__(self,accessno,name,dept):
        self.__accessno=accessno
        self.name=name
        self.dept=dept
    def display(self):
        print(self.__accessno)
        print(self.name)
        print(self.dept)

c1=company(1234,'murali','mech')
c1.display()

class school():
    def __init__(self):
        self.name='divya'
    def display(self):
        print(self.name)

s1=school()
s1.display()