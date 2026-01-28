class student:
        
    def __init__ (self,name,dept,age,section,cgpa,address,history_of_arrrear):
        self.name=name
        self.dept=dept
        self.age=age
        self.section=section
        self.cgpa=cgpa
        self.address=address
        self.history_of_arrrear=history_of_arrrear
    def display(self):
        print("the name is:",self.name)
        print("dept is:",self.dept)
        print("the age is:",self.age)
        print("the section is:",self.section)
        print("the cgpa is:",self.cgpa)
        print("the address is :",self.address)
        print("the history of arrear:",self.history_of_arrrear)
        print("this is a details of the student of {}".format(self.name))

stu1=student("divya","cse",20,"c",9.0,"minjur","nil")
stu1.display()
