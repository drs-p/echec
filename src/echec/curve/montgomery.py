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


class Montgomery(abstractcurve.AbstractCurve):
    """
    An elliptic curve in Montgomery form, given by By^2 = x^3 + Ax^2 + x.
    """
    def __init__(self, name, p, A, B=1):
        A = mpz(A)
        B = mpz(B)

        super().__init__(name, p)
        assert -p < A < p
        assert -p < B < p
        assert B * (A**2 - 4) % p != 0

        self.A = A
        self.B = B
        self._Binv = invert(self.B, p)

    def __hash__(self):
        return hash((self.p, self.A, self.B))

    def __eq__(self, other):
        if not issubclass(other.__class__, self.__class__):
            return False

        if (self.p == other.p
                and (self.A - other.A) % self.p == 0
                and (self.B - other.B) % self.p == 0):
            return True
        else:
            return False

    def __str__(self):
        s = f"{self.name}: " if self.name is not None else ""
        if self.B != 1:
            s += f"Montgomery curve defined by "
            s += f"{self.B}*y^2 = x^3 + {self.A}*x^2 + x"
        else:
            s += f"Montgomery curve defined by "
            s += f"y^2 = x^3 + {self.A}*x^2 + x"
        s += f" over GF({self.p})"

        return s

    def y_squared(self, x):
        return self._Binv * (x**3 + self.A * x**2 + x) % self.p

    @classmethod
    def find_curve_from_points(cls, *points, primes=None):
        """
        Factory method: given a number of points, return a Montgomery curve
        that contains all points, or None if such a curve cannot be found.
        The optional parameter `primes` contains a list of candidates for
        the characteristic of the finite field F_p; passing this *may* allow
        the method to succeed with fewer points.
        """
        if len(points) < 3:
            return None

        # To use the technique outlined in AbstractCurve, we need to
        # generate a number of pairs (L,R) such that L = c*R (mod p)
        # for unknown (but fixed) c and p.
        #
        # From By^2 == x^3 + Ax^2 + x (mod p) we see that
        #     B * y1^2 * y2^2 == y2^2 * (x1^3 + x1) + A * x1^2 * y2^2 and
        #     B * y1^2 * y2^2 == y1^2 * (x2^3 + x2) + A * x2^2 * y1^2,
        # and hence
        #     y2^2*(x1^3+x1) - y1^2*(x2^3+x2) == A * (x1^2*y2^2 - x2^2*y1^2),
        #
        # so we can take L = y2^2*(x1^3+x1) - y1^2*(x2^3+x2)
        # and R = x1^2*y2^2 - x2^2*y1^2.
        #
        lr = [(q.y**2 * (p.x**3 + p.x) - p.y**2 * (q.x**3 + q.x),
               p.y**2 * q.x**2 - q.y**2 * p.x**2)
              for (p,q) in itertools.combinations(points[:4], 2)]

        if len(points) >= 4:
            p = cls._determine_p(lr)
            if p is not None:
                primes = [p]

        if not primes:
            return None

        max_coord = max([abs(q.x) for q in points] + [abs(q.y) for q in points])
        for p in primes:
            if max_coord >= p:
                continue

            l, r = lr[0]
            x, y = points[0].x, points[0].y
            A = invert(r, p) * l % p
            B = invert(y**2, p) * (x**3 + A*x**2 + x) % p

            curve = Montgomery(None, p, A, B)
            if all(curve.contains_point(q) for q in points):
                return curve

        return None
