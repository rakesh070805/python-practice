#syntax import module_name

#math module
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)

#random module
import random
print(random.randint(1, 10))

#datetime module
from datetime import datetime
now = datetime.now()
print(now)

from datetime import datetime,timedelta
y=datetime.now().timetuple()
print("current date and time:",datetime.now().timetuple())
print("current year:",y[0])
print("month of year:",y[1])
print("week number of the year:",datetime.now().strftime("%U"))
print("weekday of the week:",datetime.now().strftime("%w"))
print("day of year:",datetime.now().strftime("%j"))
print("day of the month:",y[2])
print("day of week:",y[6])
print(datetime.now().time())


date="14-07-2026"
d=datetime.strptime(date,"%d-%m-%Y")
print(d)


s="july 1 14 2:43pm"
d=datetime.strptime(s,"%B %d %y %H:%M%p")
print(d)


today=datetime.today()
before=today-timedelta(5)
print(before.date())


today=datetime.today().date()
print("yesterday:",today-timedelta(1))
print("today:",today)
print("tomorrow:",today+timedelta(1))


now=datetime.now()
new=now+timedelta(seconds=5)
print(now)
print("seconds 5",new)


d=datetime(2026,7,14)
print(d.strftime("%V"))


num=int(input("enter year"))
if num%4==0:
     print("leap year")
else:
    print("not leap year")






#user-defined module
def greet():
    print("welcome to  python")

#main.py
mumodule.greet()
