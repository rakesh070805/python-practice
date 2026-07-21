class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")
for i in (Cat(), Dog()):
    i.sound()




class cal:
    def add(s,a,b):
        print(a+b)
    def mul(s,a):
        print(a*2)
obj=cal()
obj.add("ram"," kumar")
obj.mul("rakesh")




class stu:
    def __init__(s,name):
        s.name=name
    def __len__(s):
        return len(s.name)
obj=stu("rakesh")
print(len(obj))



class bird:
    def __init__(s,n):
        s.n=n
    def make_sound(s):
        print("bird sound")
class parrot(bird):
    def make_sound(s):
        print(s.n,"bird2")
class sparrow(parrot):
    def make_sound(s):
        print(s.n,"bird3")
p=parrot("parrot")
s=sparrow("sparrow")
p.make_sound()
s.make_sound()



class india:
    def __init__(s):
        s.name="india"
        
    def capital(s):
        return "new delhi"
    
    def language(s):
        return "hindi"
class usa(india):
    def __init__(s):
        s.name="usa"
        
    def capital(s):
        return "washington"
    
    def language(s):
        return "english"
class uk(usa):
    def __init__(s):
        s.name="uk"
        
    def capital(s):
        return "london"
    
    def lanfuage(s):
        return "english"
def countrys(country):
    print("country:",country.name)
    print("capital:",country.capital())
    print("language:",country.language())
    print()

countrys(india())
countrys(usa())
countrys(uk())
