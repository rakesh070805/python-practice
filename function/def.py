def welcome():
   print("welcome")
welcome()



def wel(name):
    print("welcome",name)
wel("akash")


def ti():
    print("your login time")
    return 10
print(ti())

a=10
def session(a):
    return a+1
b=session(a)
print("session end time",b)


def session(**a):
    for i,j in a.items():
       print(i,j)
b=session(b=10,a=30,c=40,d=50)
print("session end time",b)


a=5
def session(*a,b=100,c=500):
    sum=0
    for i in a:
        sum+=i
    print(sum*b/c)
session(a)


def add(a,b):
    print(a+b) 
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
   print(a/b)
a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=input("enter (1.add,2.sub,3.mul,4.div):")
if c=="1":
    print("total:",add(a,b))
elif c=="2":
    print("total:",sub())
elif c=="3":
    print("total:",mul())
elif c=="4":
    print("total:",div())



