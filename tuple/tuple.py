#syntax tuple_name=(item1,item2,item3)

fruits=("apple","banana","mango")
print(fruits)

#access tuple element
num=(10,20,30,40)
print(num[0])
print(num[2])

#tuple with different data types
date=("rakesh",20,85.5,true)
print(data)

#count and index
num=(10,20,30,40)
print(num.count(20))
print(num.index(30))

#length of a tuple
fruits=("apple","banana","mango")
print(len(fruits))

#convert tuple to list
t=(10,20,30)
l=list(t)
print(l)

#loop through a tuple
fruits=("apple","banana","mango")
for fruit in fruits:
    print(fruit)
