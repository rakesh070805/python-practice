class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()



class personal:
    def __init__(self,name,mail,mobile,address):
        self.name=name
        self.mail=mail
        self.mobile=mobile
        self.address=address
    def display_personal(self):
        print("name:",self.name)
        print("mail:",self.mail)
        print("mobile:",self.mobile)
        print("address:",self.address)
    
    
class educational(personal):
    def __init__(self,eng,tam,sci,soc):
        self.total=eng+tam+sci+soc
        self.percentage=self.total/500*100
    def display_educational(self):
        print("total:",self.total)
        print("percentage:",self.percentage)
ob=educational(50,60,70,80)
obj=personal("rakesh","rakesht070805@gmail.comm","6380038560","madurai")
obj.display_personal()
ob.display_educational()
