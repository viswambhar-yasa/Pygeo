from pygeo.objects import Point, Ray, Vector, Sphere, Triangle
import numpy as np

def intersect(first_object, second_object):
    """function to check for objects belonging to which class and call the referene function accordingly
    Input: 
        first_object    = Should be a Ray object
        second_object   = Should be a Sphere or Traingle"""
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

    """check the intersection between ray and sphere 
    Returns : points of intersection and number of intersections
    
    """
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
    """check the intersection between ray and Traingle 
    Returns : points of intersection and number of intersections
    """
    O=ray._origin
    D=ray._direction
    ray_line=D-O

    A=triangle._v1
    B=triangle._v2
    C=triangle._v3
    AB=B-A
    #print(AB)
    AC=C-A 
    #print(AC)
    BC=C-B
    Normal=AB.cross(AC)

    ND=Normal*ray_line
    if ND==0:
        "Triangle and ray are parallel"
        return 0,[0]
    distance=Normal*A
    t=((Normal*O)+distance)/ND
    if t<0 :
        return 0,[0]
    else :
        intercepts=O+(ray_line)*t
       # V1=Normal.cross(AB)
        #if (V1*(intercepts-A))<0:
         #   return 0,[0]
       # V2=Normal.cross(BC)
        #if (V2*(intercepts-B))<0:
         #   return 0,[0]
        #V3=Normal.cross(AC)
        #if(V3*(intercepts-A))<0:
         #   return 0,[0]
        return 1,[intercepts]
    

'''
t = Triangle((1, 0, 0), (0, 1, 0), (0, 0, 1))
r1 = Ray((0, 0, 0), (1, 1, 1))
d,output = intersect(r1, t)
print(output)
'''







