def add(a,b,c):#parameters
    return(a+b+c)

print(add(2,3,4))#arguments
#3types of arguments
#1.positional
print(add(3,4,5))

#2.keyword arguments
print(add(b=9,a=8,c=3))

#default
def sum(a,b=100):#default ,default values comes at last
    return(a+b)

print(sum(2))