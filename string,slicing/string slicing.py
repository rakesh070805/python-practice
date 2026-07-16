a=input("enter ur name:")
print("start 3 letter:",a[:3])



a=input("enter ur name:")
print("last 5 letter:",a[-5:])


a=input("enter ur name:")
print(a[2:7])


a=input("enter ur name:")
print(a[::-1])


a=[1,2,3,4]
a.remove(1)
print(a)


a=[1,2,3,4,]
a.pop()
print(a)

a=[1,2,3,4,5]
print(a[1:4])


a="hi i am rakesh"
b=a.split()
print(b)

a="hi i am rakesh \n ur name"
b=a.splitlines()
print(b)


a="how are you"
print(a[:len(a)//2])

a="how are you"
print(a[len(a)//2:])
