Num=int(input("Enter a number:"))
count=0
for i in range(1,Num+1,1):
    if (Num%i==0):
        count=count+1

if(count>2):
    print(Num,"is not prime")
else:
    print(Num,"is prime")

