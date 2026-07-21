try:
        
    a=int(input("enter num:"))
    b=int(input("enter num:"))
    c=a/b
except:
    print("error: division by zero undefined")
else:    
    print(c)





def add(a,b):
    print(a+b)
try:
    a=int(input("enter num:"))
    b=int(input("enter num:"))
    ans=add(a,b)
    print(ans)
except:
    print("error: value error")


try:
    a=input("enter num")
    
    if a.isdigit():
          print(int(a))
    else:
        raise ValueError("invalid integer")

except ValueError as e:
    print(e)


try:
        
    a=input("enter num:")
    b=input("enter num:")

    if a.isdigit() and b.isdigit():
       print(int(a)+int(b))
    else:
        raise TypeError("enter only number")
except TypeError as e:
    print(e)


try:
    num=[10,20,30,40]
    a=int(input("enter num:"))
    if a in num:
          print("value found",a)
    else:
        raise ValueError("value not found")
except ValueError as e:
    print(e)


