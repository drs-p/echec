import random

from sympy.ntheory.generate import nextprime as next_prime
from sympy.ntheory.residue_ntheory import sqrt_mod

from echec.point import Point


def random_point(upper):
    "Generate a random point with q.x, q.y < upper."
    x, y = [random.randint(0, upper-1) for _ in range(2)]
    return Point(x, y)


def random_point_on_curve(curve):
    "Generate a random point on the given elliptic curve."
    x = random.randint(0, curve.p - 1)
    while not curve.contains_xcoord(x):
        x = (x + 1) % curve.p
    y = sqrt_mod(curve.y_squared(x), curve.p)
    return Point(x, y)
