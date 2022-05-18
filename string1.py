string1 = "I am fine"
x=len(string1)
print("the length of string is :"+str(x) )
for i in range(x):
    print(string1[i])
print("\n")

for i in range(x):
    print("{}is stored at index {}".format(string1[i],i))
