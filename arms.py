num=int(input("Enter a number to find if its armstrong :"))
number=num
add=0 

while number>0:  
    rem=number%10
    add=add+rem**3
    number=number//10
    
if (num==add):
    print("It's an Armstrong number")
elif(add!=num):
    print("It's not an armstrong number")
              
              
              
