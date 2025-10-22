import math

class Circle:
    
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
r = float(input("Enter the radius of the circle:"))

circle1 = Circle(r)

print(f"\nFor a circle with radius {r}:")
print(f"Area ={circle1.area():.2f}")
print(f"Perimeter = {circle1.perimeter():.2f}")