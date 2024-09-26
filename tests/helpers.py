#   ------------------------------------------------------------------------
#
#   Copyright (C) 2024  Marc Penninga
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   ------------------------------------------------------------------------


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
