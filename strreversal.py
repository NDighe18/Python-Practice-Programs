#string reversal
str1=input("Enter any string : ")
x=len(str1)
str2=""
for i in range(x-1,-1,-1):
    str2 = str2 + str1[i]
print(str2)    
