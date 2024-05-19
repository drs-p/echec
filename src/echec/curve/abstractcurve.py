import itertools

from .numbertheory import *


class AbstractCurve:
    """
    An (abstract) elliptic curve, defined over a prime field F_p.
    """
    def __init__(self, name, p):
        p = mpz(p)

        assert p > 6 and p.is_prime()

        self.name = name
        self.p = p

    def __repr__(self):
        return f"{self.__class__}({self.__dict__})"

    def y_squared(self, x):
        """Compute and return the value of y^2 from x."""
        raise NotImplementedError

    def contains_point(self, q):
        """
        Test if the point q is an element of the curve.

        This default implementation only works for subclasses
        that implement the method `y_squared(x)`.
        """
        x, y = q.x, q.y
        p = self.p
        return (-p < x < p
                and -p < y < p
                and self.y_squared(x) == y**2 % p)

    def contains_xcoord(self, x):
        """
        Test if the curve contains an element with x-coordinate x.

        This default implementation assumes that any subclass
        implements the method `y_squared(x)`.
        """
        p = self.p

        return (-p < x < p
                and legendre(self.y_squared(x), p) == 1)

    @classmethod
    def find_curve_from_points(cls, *points, primes=None):
        """
        Factory method: given a number of points, return an elliptic curve
        E/F_p that contains all points, or None if such a curve cannot
        be found. The optional parameter `primes` contains a list of
        candidates for the characteristic of the finite field F_p;
        passing this *may* allow the method to succeed with fewer points.
        """
        raise NotImplementedError

    @staticmethod
    def _determine_p(lr):
        """
        Helper method for use in subclasses' implementations of
        find_curve_from_points().

        Given a list of (L,R) pairs such that L == c*R (mod p)
        for unknown (but fixed) curve parameters c and p, return the prime p,
        or None if p cannot be found (which might happen for several reasons,
        including not enough (L,R) pairs).

        From L = c*R (mod p), L' = c*R' (mod p), we see that L * R' - L' * R
        is a (generally large) multiple of p.  We find as many such multiples
        as we can, take their gcd, remove any small prime factors and check
        if the result is a prime. If so, we have found p.
        """
        multiples = [l1*r2 - l2*r1
                     for ((l1,r1),(l2,r2)) in itertools.combinations(lr, 2)]
        p = abs(gcd(*multiples))
        p = remove_small_prime_factors(p)
        if p > 1 and p.is_prime():
            return p
        else:
            return None
