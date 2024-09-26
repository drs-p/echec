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


import itertools

from . import abstractcurve
from .numbertheory import *


class Weierstrass(abstractcurve.AbstractCurve):
    """
    A (twisted) Weierstrass curve, given by dy^2 = x^3 + ax + b over F_p.
    """
    def __init__(self, name, p, a, b, d=1):
        a = mpz(a)
        b = mpz(b)
        d = mpz(d)

        super().__init__(name, p)
        assert -p < a < p
        assert -p < b < p
        assert -p < d < p

        self.a = a
        self.b = b
        self.d = d
        self._dinv = invert(d, p)

    def __hash__(self):
        return hash((self.p, self.a, self.b, self.d))

    def __eq__(self, other):
        if not issubclass(other.__class__, self.__class__):
            return False

        if (self.p == other.p
                and (self.a - other.a) % self.p == 0
                and (self.b - other.b) % self.p == 0
                and (self.d - other.d) % self.p == 0):
            return True
        else:
            return False

    def __str__(self):
        s = f"{self.name}: " if self.name is not None else ""
        if self.d != 1:
            s += f"Twisted Weierstrass curve defined by "
            s += f"{self.d}*y^2 = x^3 + {self.a}*x + {self.b}"
        else:
            if self.a != 0:
                s += f"Weierstrass curve defined by "
                s += f"y^2 = x^3 + {self.a}*x + {self.b}"
            else:
                s += f"Weierstrass curve defined by "
                s += f"y^2 = x^3 + {self.b}"
        s += f" over GF({self.p})"

        return s

    def y_squared(self, x):
        return self._dinv * (x**3 + self.a * x + self.b) % self.p

    @classmethod
    def find_curve_from_points(cls, *points, primes=None):
        """
        Factory method: given a number of points, return a Weierstrass curve
        that contains all points, or None if such a curve cannot be found.
        The optional parameter `primes` contains a list of candidates for
        the characteristic of the finite field F_p; passing this *may* allow
        the method to succeed with fewer points.
        """

        # We first try to find a (regular) Weierstrass curve that contains
        # all points; only when that fails do we look for (computationally
        # more expensive) twisted curves.
        curve = cls._find_weierstrass(*points, primes=primes)
        if curve is None:
            curve = cls._find_twisted_weierstrass(*points, primes=primes)

        return curve

    @classmethod
    def _find_weierstrass(cls, *points, primes=None):
        if len(points) < 3:
            return None

        # To use the technique outlined in AbstractCurve, we need to
        # generate a number of pairs (L,R) such that L = c*R (mod p)
        # for unknown (but fixed) c and p.
        #
        # Subtracting y2^2 = x2^3 + ax2 + b from y1^2 = x1^3 + ax1 + b
        # gives (y1^2 - y2^2) - (x1^3 - x2^3) = a(x1 - x2),
        # so we can take L = (y1^2 - y2^2) - (x1^3 - x2^3) and R = x1 - x2.
        #
        lr = [((p.y**2 - q.y**2) - (p.x**3 - q.x**3), p.x - q.x)
              for (p,q) in itertools.combinations(points[:4], 2)]

        if len(points) >= 4:
            p = cls._determine_p(lr)
            if p is not None:
                primes = [p]

        if not primes:
            return None

        max_coord = max([abs(q.x) for q in points]
                        + [abs(q.y) for q in points])
        for p in primes:
            if max_coord >= p:
                continue

            l, r = lr[0]
            x, y = points[0].x, points[0].y
            a = invert(r, p) * l % p
            b = (y**2 - x**3 - a*x) % p

            curve = cls(None, p, a, b)
            if all(curve.contains_point(q) for q in points):
                return curve

        return None

    @classmethod
    def _find_twisted_weierstrass(cls, *points, primes=None):
        if len(points) < 4:
            return None

        # We use the same technique as in _find_weierstrass(),
        # but the extra unknown curve parameter d makes things a bit
        # more complicated.
        pairs = itertools.combinations(points[:5], 2)
        quadruples = itertools.combinations(pairs, 2)
        lr = [((p1.y**2 - p2.y**2) * (p3.x**3 - p4.x**3)
               - (p3.y**2 - p4.y**2) * (p1.x**3 - p2.x**3),
               (p1.y**2 - p2.y**2) * (p3.x - p4.x)
               - (p3.y**2 - p4.y**2) * (p1.x - p2.x))
              for ((p1,p2),(p3,p4)) in quadruples]

        if len(points) >= 5:
            p = cls._determine_p(lr)
            if p is not None:
                primes = [p]

        if not primes:
            return None

        max_coord = max([abs(q.x) for q in points]
                        + [abs(q.y) for q in points])
        for p in primes:
            if max_coord >= p:
                continue

            l, r = lr[0]
            x1, y1 = points[0].x, points[0].y
            x2, y2 = points[1].x, points[1].y
            a = invert(r, p) * (p - l) % p
            d = (invert(y1**2 - y2**2, p)
                 * (x1**3 - x2**3 + a*(x1 - x2))) % p
            b = (d * y1**2 - x1**3 - a*x1) % p

            curve = cls(None, p, a, b, d)
            if all(curve.contains_point(q) for q in points):
                return curve

        return None
