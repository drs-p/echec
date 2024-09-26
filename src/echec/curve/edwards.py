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


class Edwards(abstractcurve.AbstractCurve):
    """
    A (twisted) Edwards curve, given by tx^2 + y^2 = 1 + dx^2y^2.

    A twisted Edwards curve has an equivalent representation
    in short Weierstrass form, given by:

        a = k^2 - 3*l^2 (mod p),
        b = 2*l^3 - l*k^2 (mod p),

    where:

        k = (t - d)/4 (mod p),
        l = (t + d)/6 (mod p).

    Coordinate transformations are defined as follows:

        (u,v) --> (x,y) = (k(1 + v)/(1 - v) + l, k(1 + v)/((1 - v)u)),
        (x,y) --> (u,v) = ((x - l)/y, (x - l - k)/(x - l + k)).

    """
    def __init__(self, name, p, d, t=1):
        d = mpz(d)
        t = mpz(t)

        super().__init__(name, p)
        assert d not in [0, 1] and -p + 1 < d < p
        assert t != 0 and -p < t < p

        self.d = d
        self.t = t

    def __hash__(self):
        return hash((self.p, self.d, self.t))

    def __eq__(self, other):
        if not issubclass(other.__class__, self.__class__):
            return False

        if (self.p == other.p
                and (self.d - other.d) % self.p == 0
                and (self.t - other.t) % self.p == 0):
            return True
        else:
            return False

    def __str__(self):
        s = f"{self.name}: " if self.name is not None else ""
        if self.t != 1:
            s += f"Twisted Edwards curve defined by "
            s += f"{self.t}*x^2 + y^2 = 1 + {self.d}*x^2*y^2"
        else:
            s += f"Edwards curve defined by "
            s += f"x^2 + y^2 = 1 + {self.d}*x^2*y^2"
        s += f" over GF({self.p})"

        return s

    def y_squared(self, x):
        return (
                invert(1 - self.d * x**2, self.p) * (1 - self.t * x**2)
               ) % self.p

    @classmethod
    def find_curve_from_points(cls, *points, primes=None):
        """
        Factory method: given a number of points, return an Edwards curve
        that contains all points, or None if such a curve cannot be found.
        The optional parameter `primes` contains a list of candidates for
        the characteristic of the finite field F_p; passing this *may*
        allow the method to succeed with fewer points.
        """
        if len(points) < 3:
            return None

        # To use the technique outlined in AbstractCurve, we need to
        # generate a number of pairs (L,R) such that L = c*R (mod p)
        # for unknown (but fixed) c and p.
        #
        # From tx^2 + y^2 == 1 + dx^2y^2 (mod p), we see that
        #     t*x1^2*x2^2 + x2^2*(y1^2-1) == d*x1^2*x2^2*y1^2 and
        #     t*x1^2*x2^2 + x1^2*(y2^2-1) == d*x1^2*x2^2*y2^2
        # and hence
        #     x1^2*(1-y2^2) + x2^2*(y1^2-1) == d*x1^2*x2^2*(y1^2-y2^2)
        #
        # so we can take L = x1^2*(1-y2^2) - x2^2*(1-y1^2)
        # and R = x1^2*x2^2*(y1^2-y2^2).
        #
        lr = [(p.x**2 * (1 - q.y**2) + q.x**2 * (p.y**2 - 1),
               p.x**2 * q.x**2 * (p.y**2 - q.y**2))
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
            xx, yy = points[0].x**2, points[0].y**2
            d = invert(r, p) * l % p
            t = invert(xx, p) * (1 + d*xx*yy - yy) % p

            curve = Edwards(None, p, d, t)
            if all(curve.contains_point(q) for q in points):
                return curve

        return None
