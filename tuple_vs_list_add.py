
t1=(4,6)               #tuple addition
print(t1)
print(id(t1))
t2=(6,8)
t1=t1+t2
print(t1)
print(id(t1))

print("\n")

l1=[4,6]               #list addition
print(l1)
print(id(l1))
l2=[6,8]
l1=l1+l2
print(l1)
print(id(l1))

#id of list and tupple are changed after addition
print("\n")

l3 = [1,2,3,4]
print(l3)
print(id(l3))
l3.append(12)
print(l3)
print(id(l3))
#id of list is same after adding elements in it through append
