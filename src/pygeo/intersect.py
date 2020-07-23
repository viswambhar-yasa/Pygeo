from pygeo.objects import Point, Ray, Vector, Sphere, Triangle
import numpy as np

def intersect(first_object, second_object):
    if isinstance(first_object,Ray) & isinstance(second_object,Sphere):
        d,intercepts=_intersect_ray_with_sphere(first_object, second_object)
        return d,intercepts
    elif  isinstance(first_object,Ray) & isinstance(second_object,Triangle):
        d,intercepts=_intersect_ray_with_triangle(first_object, second_object)
        return d,intercepts
    else:
        print("could not execute")
        return NotImplemented

def _intersect_ray_with_sphere(ray, sphere):
    ray_origin=ray._origin
    ray_direction=ray._direction
    line=ray_direction-ray_origin
    circle_center=sphere._center
    radius=sphere._radius
    

    a=line*line
    co=(circle_center-ray_origin)
    b=2*(line*co)
    c=(co*co)-((radius)**2)

    delta=(b**2)-4*(a*c)
    if delta<0:
        return 0,[0]
    elif delta>0:
        d1=(-2*b+(np.sqrt(delta)))/(2*a)
        d2=(-2*b-(np.sqrt(delta)))/(2*a)
        intercept1=ray_origin+((ray_direction-ray_origin)*d1)
        intercept2=ray_origin+((ray_direction-ray_origin)*d2)
        intercepts=[intercept1,intercept2]
        d=2
        return d,intercepts
    else :
        d1=(-2*b+(np.sqrt(delta)))/2*a
        intercepts=[ray_origin+((ray_direction-ray_origin)*d1)]
        d=1
        return d,intercepts




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





r1 = Ray((100, 100, 100), (200, 200, 100))
s1 = Sphere((0, 0, 0), 5)
d,intercepts = intersect(r1, s1)
print(d,intercepts)
intercepts_analytical = [0]
d_analytical=0
print((intercepts == intercepts_analytical) and (d_analytical==d) )







