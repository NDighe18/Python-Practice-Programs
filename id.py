l=[1,2,3]
print(l)
print(id(l))
l.append(12)
print(id(l))

print("\n")

t1=[1,2,3]
t2=[4,5]
print(id(t1))
print(t1)
t1=t1+t2
print(id(t1))
print(t1)

print("\n")

l1=[1,2,3,4]
print(l1)
print(id(l1))
l1.append(12)
print(l1)
print(id(l1))
