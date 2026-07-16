a=int(input("enter value:"))
if a>0:
    print("possitive")
elif a<0:
    print("negative")
else:
    print("zer0")




a=int(input("enter value"))
if a%2==0:
   print("even")
else:
  print("odd")



a=int(input("enter value"))
b=int(input("enter value"))
c=int(input("enter value"))

if a>b:
    print("greater a:",a)
elif b>c:
    print("greater b:",b)
else:
    print("greater c:",c)




a=int(input("enter value"))
if a>=90 and a<=100:
    print("a")
elif a>=80 and a<=89:
    print("b")
elif a>=70 and a<=79:
    print("c")
elif a>=50 and a<=69:
    print("d")
else: print("fail")




a=int(input("enter value"))
if a>=0 and a<=100:
    print(a*2)
elif a>=101 and a<=200:
    print(a*4)
elif a>=200:
    print(a*6)





a=input("enter your name:")
b=input("enter your pass:")
if a=="admin" and b=="python123":
    print("login sucessful")
else:print("invalid name or pass")

