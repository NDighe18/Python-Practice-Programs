num=int(input("Enter a number to calculate it's Factorial : "))
fact=1
for i in range(1,num+1,1):
    fact=fact*i
print("Factorial of ",num, "is :",fact)
