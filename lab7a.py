
import math


class Shape:
    def __init__(self):
        self.area = 0
        self.name = ""

    def showArea(self):
        print("The area of the", self.name, "is", self.area, "units")


class Circle(Shape):
    def __init__(self, radius):
        self.area = 0
        self.name = "Circle"
        self.radius = radius

    def calcArea(self):
        self.area = math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, lengths, breadth):
        self.area = 0
        self.name = "Rectangle"
        self.length = lengths
        self.breadth = breadth

    def calcArea(self):
        self.area = self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.area = 0
        self.name = "Triangle"
        self.base = base
        self.height = height

    def calcArea(self):
        self.area = self.base * self.height / 2

r = int(input("enter the radius "))
c1 = Circle(r)
c1.calcArea()
c1.showArea()

l= int(input("enter the length "))
b= int(input("enter the breadth "))
r1 = Rectangle(l, b)
r1.calcArea()
r1.showArea()

b= int(input("enter the base and height "))
h= int(input("enter the base and height "))
t1 = Triangle(b, h)
t1.calcArea()
t1.showArea()
