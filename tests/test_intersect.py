from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Point, Vector, Ray, Sphere, Triangle

import pytest


# intersect
def test_intersect_ray_sphere():
    r1 = Ray((0, 0, 0), (5, 0, 0))
    r2 = Ray((0, 0, 0), (5, 0, 0))
    intercepts = intersect(r1, r2)
    expected = NotImplemented
    assert (expected == intercepts) is True


# _intersect_ray_with_sphere


def test_intersect_ray_with_sphere_true():
    r1 = Ray((0, 0, 0), (10, 0, 0))
    s1 = Sphere((0, 0, 0), 5)
    d,intercepts = intersect(r1, s1)
    intercepts_analytical = [Point([5.0, 0.0, 0.0]), Point([-5.0, 0.0, 0.0])]
    d_analytical = 2
    assert ((intercepts == intercepts_analytical) and (d_analytical==d) )is True

def test_intersect_no_intersect_ray_with_sphere_true():
    r1 = Ray((100, 100, 100), (200, 200, 100))
    s1 = Sphere((0, 0, 0), 5)
    d,intercepts = intersect(r1, s1)
    intercepts_analytical = [0]
    d_analytical=0
    assert ((intercepts == intercepts_analytical) and (d_analytical==d) )is True

def test_intersect_ray_with_sphere_false():
    r1 = Ray((0, 0, 0), (1, 1, 1))
    s1 = Sphere((10, 10, 10), 5)
    d,intercepts = intersect(r1, s1)
    intercepts_analytical = [Point([5.0, 0.0, 0.0]), Point([-5.0, 0.0, 0.0])]
    d_analytical = 2
    assert ((intercepts == intercepts_analytical) and (d_analytical==d) ) is False


# _intersect_ray_with_triangle

def test_intersect_ray_with_triangle_false():
    t = Triangle((1, 0, 0), (0, 1, 0), (0, 0, 1))
    r1 = Ray((0, 0, 0), (-1, -1, -1))
    d,intercepts = intersect(r1, t)
    intercepts_analytical = Point([0.3333333333333333, 0.3333333333333333, 0.3333333333333333])
    d_analytical=1
    assert ((intercepts == intercepts_analytical) and (d_analytical==d) ) is False


def test_intersect_ray_with_triangle_true():
    t = Triangle((1, 0, 0), (0, 1, 0), (0, 0, 1))
    r1 = Ray((0, 0, 0), (1, 1, 1))
    d,intercepts = intersect(r1, t)
    intercepts_analytical = Point([0.3333333333333333, 0.3333333333333333, 0.3333333333333333])
    d_analytical=1
    assert ((intercepts == intercepts_analytical) and (d_analytical==d) ) is True