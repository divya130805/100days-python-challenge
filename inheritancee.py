#multi level inheritance
class school():
    def __init__(self,data):
        self.data=data
class student1(school):
    def detail(self):
        print("my name is:",self.data)
class student2(school):
    def detail2(self):
        print("my name is:",self.data)

stu1=student1("divya")
stu1.detail()
#single level inheritance
class stalin():
    def cm(self):
        print("he is 1st cm in tamil nadu!!")
class uthiyanithi(stalin):
    def asst_cm(self):
        print("asst cm by the power off father!!")
class inbanithi(uthiyanithi):
    def owner_gaint(self):
        print("he is a owner with a help of father")


inba=inbanithi()
inba.asst_cm()
inba.owner_gaint()
uthai=uthiyanithi()
uthai.cm()
