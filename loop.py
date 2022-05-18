n=int(input("Enter value of n: "))
for i in range(1,11,1) :
      print(n,"*",i,"=",i*n)
     
print("\n")

n=int(input("Enter value of n: "))
m=n*10
count=1
for i in range (n,m+1,n):
    print("{}*{}={}".format(n,count,i))
    count=count+1
