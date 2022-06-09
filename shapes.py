from re import A


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        a = 3.14*self.radius**2
        return f"The area is {a}"
    def circumfrence(self):
        c = 2*3.14*self.radius
        return c

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        a = self.side**2
        return a

    def perimetre(self):
        p = 4*self.side
        return p

class Rectangle:
    def __init__(self, w, l):
        self.w = w
        self.l = l
    def area (self):
        a = self.w*self.l
        return a
    def perimetre(self):
        p = 2*(self.w+self.l)
class Sphere:
    def __init__(self, r):
        self.r = r
    def surface_area (self):
        a = 4*3.14*self.r**2
        return a
    def volume(self):
        v =  4/3(3.14*self.r**3)
        return     