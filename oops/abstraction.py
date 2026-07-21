from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Child Class
class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of Rectangle:", self.length * self.breadth)


# Child Class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle:", 3.14 * self.radius * self.radius)


# Create Objects
r = Rectangle(10, 5)
c = Circle(7)

print("----- Shape Areas -----")
r.area()
c.area()
