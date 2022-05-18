list1 = [2,13,42,524,331,452,321,22]
list_even = []

print(list1)
print(list_even)

for i in list1:
    if i%2==0:
        list_even.append(i)

print(list_even)

""" OR """

def even(n):
    return n%2==0

list1 = [2,13,42,524,331,452,321,22]
list_even = list(filter(even,list1))
print(list1,list_even)

""" OR """

list_even = list(filter(lambda x: x%2==0,list1))    #(function,iteratable)
print(list_even)

#map function

list_even2 = list(map(lambda x: x*2,list_even)) # multiplying each element of even list by 2
print(list_even2)

#reduce function
from functools import reduce
sum_even = reduce(lambda x,y : x+y,list_even2)  #need to import reduce
print(sum_even)
