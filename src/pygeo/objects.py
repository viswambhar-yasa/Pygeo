import numpy as np
import math as m
import pytest 

class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False



class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Vector({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def cross(self,other):
        if isinstance(other,Vector):
            cross=np.cross(self._vector,other._vector)
            return Vector(cross)
        if isinstance(other,Point):
            cross=np.cross(self._vector,other._point)
            return Vector(cross)
        return NotImplemented

    def magnitude(self):
        c=np.linalg.norm(self._vector)
        return c  

    def unit_vector(self):
        return Vector((1/self.magnitude())*self._vector)
    
    def __mul__(self,other):
        if isinstance(other,Vector):
            return np.dot(self._vector,other._vector)
        if isinstance(other,Point):
            return np.dot(self._vector,other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray(Point,Vector):
    """A ray."""

    def __init__(self,origin,direction): 
        if Point(origin)==Point(direction):
            self._origin=()
            self._direction=()
            raise Exception("The end point and direction should not be same")
        else:
            self._origin=Point(origin)
            self._direction=Point(direction)
            self._r=self._direction-self._origin

    def magnitude(self):
        c=Vector.magnitude((self._r))
        return c
    
    def unit_vector(self):
        u=Vector.unit_vector((self._r))
        return u
    


    def __repr__(self):
        return f"Ray{self._origin,self._direction}"
    
    def __eq__(self,other):
        if isinstance(other,Ray):
            return np.array_equal(other._origin,self._origin) & np.array_equal(other._direction,self._direction)
        return False



class Sphere(Point):
    """A sphere."""
    def __init__(self,origin,radius):
        if radius<=0:
            raise Exception("Radius cannot be negative or zero")
        else:
            self._origin=Point(origin)
            self._radius=radius

    def __repr__(self):
        return f"Sphere{self._origin,self._radius}"

    def area(self):
        area=(4/3)*(m.pi)*(self._radius)**3
        return area

    def circumfernece(self):
        return (4*m.pi*self._radius**2)

    def __eq__(self,other):
        if isinstance(other,Sphere):
            return np.array_equal(other._origin,self._origin)& (other._radius==self._radius)
        return



class Triangle(Point,Vector):
    """A triangle."""
    def __init__(self,vertice1,vertice2,vertice3):  
        self._v1=Point(vertice1)
        self._v2=Point(vertice2)
        self._v3=Point(vertice3)
        self._AB=self._v2-self._v1
        self._BC=self._v3-self._v2
        self._AC=self._v3-self._v1
        a,b,c=self.sidelengths()
        if  ((a + b) > c)  &     ((a + c) > b )  &    ((b + c) > a) :
            pass
        else:
            raise Exception("The vertices are collinear")

    def __repr__(self):
        return f"Triangle{self._v1,self._v2,self._v3}"

    def sidelengths(self):
        a=Vector.magnitude(self._AB)
        b=Vector.magnitude(self._BC)
        c=Vector.magnitude(self._AC)
        return a,b,c

    def perimeter(self):
        a,b,c=self.sidelengths()
        p=(a+b+c)
        return p

    def area(self):
        a,b,c=self.sidelengths()
        s=a+b+c/3
        Area=np.sqrt((s*(s-a)*(s-b)*(s-c)))
        return Area
    
    
"""
#t=Triangle((0, 0, 0), (0, 0, 0),(0,0,10))
t=Triangle((0, 0, 0), (0, 10, 0),(0,0,10))
print(t)
print(t.sidelengths())
print(t.area())
r1 = Ray((0, 0, 0), (0, 0, 0))
print(r1.magnitude())
s1 = Sphere((1, 0, 1), 5)
print(s1.area())
#s1 = Sphere((1, 0, 1), 0)
v=Vector((1, 1, 1))
print(v.unit_vector())
print(r1)
p=Point(1)
print(p)
v=Vector((1,0,1))
print(v+p)
print(p+v)
"""
