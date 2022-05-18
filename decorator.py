from support import *

def smart_div(func):
    def inner(m,n):
        if m<n:
            m,n=n,m
        return func(m,n)
    return inner

a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=div(a,b)
div1=smart_div(div)
d=div1(a,b)

print("a= ",a)
print("b= ",b)
print("c= ",c)
print("d= ",d)

"""#writing a function such that numerator>denominator always
#changing func

def div(x,y):
    if x<y:
        x,y=y,x
    return x/y
# decorators are functions through which we can change working of current function"""

