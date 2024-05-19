import functools
import operator

from gmpy2 import gcd, invert, is_prime, legendre, mpz
import sympy.ntheory.factor_


__all__ = ["gcd", "invert", "is_prime", "legendre", "mpz",
           "remove_small_prime_factors"]


def remove_small_prime_factors(n, limit=10**6):
    """
    Remove all "small" prime factors (i.e., those not exceeding limit) from n.
    """
    factors = sympy.ntheory.factor_.factorint(n, limit=limit, multiple=True)
    large_factors = [p for p in factors if p > limit]

    return functools.reduce(operator.mul, large_factors, mpz(1))
