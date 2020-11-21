import math as m

class Circle():

    def __init__(self, radius = 1.0, color = "red"):
        self.radius = radius
        self.color = color
    
    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return (f"Radius: {self.getRadius()} and the color of circle is \nColor: {self.getColor}")
    
    def getArea(self):
        return (m.pi * self.getRadius()**2)

class Cylinder(Circle):

    def __init__(self, height = 1.0, radius = 1.0, color = "red"):
        self.height = height
        super().__init__(radius, color)
        
    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def __str__(self):
        return (f"Height: {self.height}\nRadius: {self.radius}\nColor: {self.color}")

    def getVolume(self):
        return (self.getArea() * self.height)
c