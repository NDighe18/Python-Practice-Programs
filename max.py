a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
if a==b==c:
    print("all are equal")
elif (a==b) and (a==b)>c:
    print(a,"and",b,"are equal and greater than",c)
else :
    print(a,"and",b,"are equal and smaller than",c)
if (a==c) and (a==c)>b:
    print(a,"and",c,"are equal and greater than",b)
else :
    print(a,"and",c,"are equal and smaller than",b)    
if (c==b) and (c==b)>a:
    print(c,"and",b,"are equal and greater than",a)
else :
    print(c,"and",b,"are equal and smaller than",a)
if a>b and a>c :
    print(a,"is max")
elif b>a and b>c :
    print(b,"is max")
else :
    print(c,"is max")
