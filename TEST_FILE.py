from pygeo.objects import Point,Vector,Ray,Sphere,Triangle

from pygeo.intersect import intersect

"""To check if the installation of the package is done and all packages are running"""

r1 = Ray((0, 0, 0), (10, 0, 0))
s1 = Sphere((0, 0, 0), 5)
d,intercepts = intersect(r1, s1)
print('The ',r1, 'intersects ',s1,'at',intercepts)

t = Triangle((1, 0, 0), (0, 1, 0), (0, 0, 1))
r1 = Ray((0, 0, 0), (1, 1, 1))
d,intercepts = intersect(r1, t)
print('The ',r1, 'intersects ',t,'at',intercepts)
