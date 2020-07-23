from pygeo.objects import Point, Vector, Ray, Sphere, Triangle

import pytest
# Point.__eq__
#@pytest.mark.point
def test__point_equal__given_two_equal_points__return_true():
    assert (Point((1, 2, 3)) == Point((1, 2, 3))) is True


def test__point_equal__given_two_not_equal_points__return_false():
    assert (Point((1, 2, 3)) == Point((4, 5, 6))) is False


# Vector.__eq__
#@pytest.mark.vector
def test__vector_equal__given_two_equal_vectors__return_true():
    assert (Vector((1, 2, 3)) == Vector((1, 2, 3))) is True


def test__vector_equal__given_two_not_equal_vectors__return_false():
    assert (Vector((1, 2, 3)) == Vector((4, 5, 6))) is False


# Point.__add__
#@pytest.mark.point
def test__point_addition__given_point_and_vector__return_correct_point():
    """The result of a vector being added to a point is a point."""
    assert Point((0, 1, 2)) + Vector((3, 4, 5)) == Point((3, 5, 7))


# Point.__radd__

def test__point_right_addition__given_vector_and_point__return_correct_point():
    """The result of a vector being added to a point is a point."""
    assert Vector((0, 1, 2)) + Point((3, 4, 5)) == Point((3, 5, 7))


# Point.__sub__
#@pytest.mark.vector
def test__point_subtraction__given_two_points__return_correct_vector():
    """The result of a point being subtracted from another one is a vector."""
    assert Point((0, 1, 2)) - Point((3, 4, 5)) == Vector((-3, -3, -3))


# Vector.__add__

def test__vector_addition__given_two_vector__return_correct_vector():
    """The result of a vector being added to another one is a vector."""
    assert Vector((0, 1, 2)) + Vector((3, 4, 5)) == Vector((3, 5, 7))


# Vector.__sub__

def test__vector_subtraction__given_two_vectors__return_correct_vector():
    """The result of a vector being subtracted from another one is a vector."""
    assert Vector((0, 1, 2)) - Vector((3, 4, 5)) == Vector((-3, -3, -3))
#@pytest.mark.ray
#Ray.__init__
def test_ray_init_function_point_list():
    r1 = Ray(Point((0, 0, 0)), Point((1, 0, 0)))
    expected=Ray((0, 0, 0), (1, 0, 0))
    assert (r1 == expected) is True

#Ray.__eq__
def test_ray_given_rays_equal_false():
    r1 = Ray((0, 0, 0), (1, 0, 0))
    r2 = Ray((1, 2, 0), (1, 0, 0))
    assert (r1 == r2) is False

def test_ray_given_rays_equal_true():
    r1 = Ray((1, 2, 0), (1, 0, 0))
    r2 = Ray((1, 2, 0), (1, 0, 0))
    assert (r1 == r2) is True

#@pytest.mark.sphere
#Sphere.__init__
def test_sphere_init_function_point():
    s1 = Sphere(Point((0, 0, 0)), 5)
    expected=Sphere((0,0,0),5)
    assert (s1 == expected) is True

def test_sphere_init_function_point_rad_zero():
    s1 = Sphere(Point((0, 0, 0)), 0)
    expected=NotImplemented
    assert (s1 == expected) is True


def test_sphere_given_spheres_equal_false():
    s1 = Sphere((0, 0, 0), 5)
    s2 = Sphere((0, 0, 0), 6)
    assert (s1 == s2) is False

def test_sphere_given_spheres_equal_true():
    s1 = Sphere((1, 0, 1), 5)
    s2 = Sphere((1, 0, 1), 5)
    assert (s1 == s2) is True

#@pytest.mark.triangle
#Triangle.__init__
def test_triangle_init_function_point_list():
    t1 = Triangle(Point((0,10,0)),Point((10,0,0)),Point((0,0,10)))
    t2 = Triangle((0,10,0),(10,0,0),(0,0,10))
    assert (t1 == t2) is True



#Triangle.__eq__
def test_triangle_given_triangles_equal_false():
    t1=Triangle((10, 0, 0), (10, 10, 0),(0,0,10))
    t2=Triangle((0, 0, 0), (0, 10, 0),(0,0,10))
    assert (t1 == t2) is False

def test_triangle_given_triangles_equal_true():
    t1=Triangle((10, 0, 0), (10, 0, 0),(0,0,10))
    t2=Triangle((0, 0, 0), (0, 10, 0),(0,0,10))
    assert (t1 == t2) is True