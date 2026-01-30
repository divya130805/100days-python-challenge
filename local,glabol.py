a=10#global variable
b=20
def add():
    a=100#local variable
    b=200
    print(a+b)

add()
print(a,b)


def add():
    global z#global keyword we access the varible from global inside the function
    z=z+10
    print(z)


z=10
y=20
print(z+y)
add()
