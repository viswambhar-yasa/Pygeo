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
        if isinstance(other,float) or isinstance(other,int) :
            return Vector(self._vector*other)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray(Point,Vector):
    """A ray.
    origin - input can be an array or point Ex-(0,0,0) or Point((0,1,0))
    direction -input can be an array or point Ex- (0,1,0) or Point((0,1,0))"""

    def __init__(self,origin,direction): 
        if not isinstance(origin,Point) :
            if Point(origin)==Point(direction):
                self._origin=()
                self._direction=()
                raise Exception("The end point and direction should not be same")
            else:
                self._origin=Point(origin)
                self._direction=Point(direction)
                self._t=self._direction-self._origin
        else:
            if origin==direction:
                self._origin=()
                self._direction=()
                raise Exception("The end point and direction should not be same")
            else:
                self._origin=origin
                self._direction=direction
                self._t=self._direction-self._origin

    def magnitude(self):
        c=Vector.magnitude((self._t))
        return c
    
    def unit_vector(self):
        u=Vector.unit_vector((self._t))
        return u    

    def __repr__(self):
        return f"Ray{self._origin,self._direction}"
    
    def __eq__(self,other):
        if isinstance(other,Ray):
            return np.array_equal(other._origin,self._origin) & np.array_equal(other._direction,self._direction)
        return False



class Sphere(Point):
    """A sphere.
    center - input can be an array or point Ex-(0,0,0) or Point((0,1,0))
    Radius -input can be an array or point Ex- (0,1,0) or Point((0,1,0))"""
    def __init__(self,center,radius:float):
        if radius<=0:
            raise Exception("Radius cannot be negative or zero")
        else:
            if not isinstance(center,Point):
                self._center=Point(center)
                self._radius=radius
            elif isinstance(center,Point):
                self._center=center
                self._radius=radius
            else:
                 raise Exception("Invalid input")
       

    def __repr__(self):
        return f"Sphere{self._center,self._radius}"

    def area(self):
        area=(4/3)*(m.pi)*(self._radius)**3
        return area

    def circumfernece(self):
        return (4*m.pi*self._radius**2)

    def __eq__(self,other):
        if isinstance(other,Sphere):
            return np.array_equal(other._center,self._center)& (other._radius==self._radius)
        return



class Triangle(Point,Vector):
    """A triangle. 
    vertice1 - input can be an array or point Ex-(0,0,0) or Point((0,1,0))
    vertice2 -input can be an array or point Ex- (0,1,0) or Point((0,1,0))
    vertice3 -input can be an array or point Ex- (0,1,0) or Point((0,1,0))
    """
    def __init__(self,vertice1,vertice2,vertice3): 
        if isinstance(vertice1,Point):
            self._v1=vertice1
            self._v2=vertice2
            self._v3=vertice3
        else :
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
    
    def __eq__(self,other):
        a,b,c=self.sidelengths()
        a1,b1,c1=other.sidelengths()
        if isinstance(other,Triangle):
            if (a/b==a1/b1) and (a/c==a1/c1) and (b/c==b1/c1):   
                return True
            else: 
                return False
        return NotImplemented

