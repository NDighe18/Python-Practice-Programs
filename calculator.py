#Program for creating a Calculator
print("             ----Basic CALCULATOR using Python----             ")
type_op=input("Enter the type of operation to be performed i.e unary or binary : ").lower()

if (type_op=='binary'):
    op_b=int(input("Enter the binary arithmetic operation to be performed :\n\
1.Addition\n\
2.Subtraction\n\
3.Multiplication\n\
4.Modulo\n\
5.Power of number\n\
6.Division\n"))

    num_type=input("Enter data type of numbers to be used i.e integer or Float : ").upper()

    if (num_type=='integer'):
        num1=int(input("Enter 1st number for operation : "))
        num2=int(input("Enter 2nd number for operation : "))
    else :
        num1=float(input("Enter 1st number for operation : "))
        num2=float(input("Enter 1st number for operation : "))

    def Add(x,y):
        a=x+y
        return(a)
    def Sub(x,y):
        s=x-y
        return(s)
    def Mul(x,y):
        m=x*y
        return(m)
    def Mod(x,y):
        md=x%y
        return(md)
    def Div(x,y):
        d=x/y
        return(d)
    def Power(x,y):
        p=x**y
        return(p)
        

    if (op_b==1):
        print("The Adition of ",num1," and",num2," is :")
        print(Add(num1,num2))
    elif (op_b==2) :
        print("The Subtraction of ",num1," and",num2," is :")
        print(Sub(num1,num2))
    elif (op_b==3)  :
        print("The Multiplication of ",num1," and",num2," is :")
        print(Mul(num1,num2))
    elif (op_b==4) :
        print("The Modulo of ",num1," and",num2," is :")
        print(Mod(num1,num2))
    elif(op_b==5) :
        print("Result of ",num1,"to the power ",num2,"is:")
        print(Power(num1,num2))
    elif (op_b==6) :
        if (num2==0):
            print("Division by zero is not defined")
        else :    
            print("The Division of ",num1," and",num2," is :")
            print(Div(num1,num2))
    else :
        print("OPERATION IS INVALID")         

elif (type_op=='unary') :
    op_u=int(input("Enter the unary operation to be performed :\n\
1.Square root\n\
2.square of number\n\
3.cube root\n"))

    num3=int(input("Enter number to perform unary operation : "))

    def sqroot(x):
        s=(x)**(0.5)
        return(s)
    def square(x):
        sq=x**2
        return(sq)
    def croot(x):
        cr=(x)**(1./3)
        return(cr)
        
    if (op_u==1):
        print("Square root of ",num3," is:")
        print(sqroot(num3))
    elif (op_u==2):
        print("Square of ",num3," is :")
        print(square(num3))
    elif (op_u==3):
        print("cube root of ",num3,"is:")
        print(croot(num3))
    else :
        print("OPERATION IS INVALID")



