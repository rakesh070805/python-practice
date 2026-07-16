for i in range(1,100):
    print(i)



for i in range(1,10):
    print(i,"*10=",i*10)

n=int(input("enter number:"))
sum=0
for i in range(1,5):
    sum+=i
    print("sum",sum)
    
     

n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact*=i
    print("factorial",fact)
    

n=int(input("enter number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
        else:
            print("primr")
else:
    print("not prime")

