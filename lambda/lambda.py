
c=lambda a,b:a*b
print(c(4,3))



a=lambda:4*6
print(a())


x=(1,2,3,4,5,6)
b=lambda :len(x)
print(b())


num=(1,2,3,4,5,6)
a=lambda x:x*6
for i in num: 
    print(a(i))



a=("mom","rakesh","121")
for i in a:
    if i==i[::-1]:
       print("polindrome",i)
    else:
        print("not polindrome",i) 
    


num=(1,2,3,4,5,6)
a=lambda : max(num)
print(a())
