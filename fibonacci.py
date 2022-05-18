n=int(input(("Enter no. to print Fibonacci series : ")))
a=0
b=1
c=0
print(a)
print(b)
for i in range(0,n-2,1):
    c=a+b
    a=b
    b=c
    print(c)
 
