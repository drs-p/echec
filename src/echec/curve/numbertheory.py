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
