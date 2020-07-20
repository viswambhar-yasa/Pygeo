from objects import Point, Ray, Vector, Sphere, Triangle
import numpy as np

def intersect(first_object, second_object):
    if isinstance(first_object,Ray) & isinstance(second_object,Sphere):
        intersects=_intersect_ray_with_sphere(first_object, second_object)
        return intersects
    elif  isinstance(first_object,Ray) & isinstance(second_object,Triangle):
        intersects=_intersect_ray_with_triangle(first_object, second_object)
        return intersects
    else:
        print("could not execute")
        return NotImplemented

def _intersect_ray_with_sphere(ray, sphere):
    ray_origin=ray._origin
    line=ray.unit_vector()
    circle_center=sphere._origin
    radius=sphere._radius
        
    a=line*line
    b=2*(line*(ray_origin-circle_center))
    c=((ray_origin-circle_center)*(ray_origin-circle_center))-(radius)**2

    delta=(-4*a*c+(b**2))

    if delta<0:
        return 0
    elif delta>0:
        d1=(-2*b+(np.sqrt(delta)))/2*a
        d2=(-2*b-(np.sqrt(delta)))/2*a
        print(d1,d2)
        return 2
    else :
        d=(-2*b+(np.sqrt(delta)))/2*a
        print(d)
        return 1




def _intersect_ray_with_triangle(ray, triangle):
   
    O=ray._origin
    R=ray._r
    
    A=triangle._v1
    AB=triangle._AB
    AC=triangle._AC
    Normal=AB.cross(AC)

    NR=Normal*R
    OA=Normal*(A-O)

    if (OA==0):
        if NR !=0:
            print("Ray is parallel to the triangle")
        else:
            distance=0
    else:
        distance=NR/OA
    if distance==0:
        print("Ray lies on the triangle")
        return 2
    if distance<0:
        return 0
    return 1

    
    










