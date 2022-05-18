import factorial
x=int(input("enter the total items "))
y=int(input("enter the no of items to be arranged"))
if x>y:
    result=factorial.fact(x)//factorial.fact(x-y)
    print(result)
elif x<y:
    print(" Error!, x should be greater than y")
