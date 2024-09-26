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

from echec import echec
from echec.curve import *
from tests.helpers import next_prime, random_point, random_point_on_curve

RANDOM_PRIMES = [next_prime(random.randint(2**(nbits-1), 2**nbits))
                 for nbits in [256, 384, 512]]


def make_weierstrass(p, twist=False):
    a = random.randint(1, p-1)
    b = random.randint(1, p-1)
    d = random.randint(2, p-1) if twist else 1
    curve = weierstrass.Weierstrass(None, p, a, b, d)
    points = [random_point_on_curve(curve) for _ in range(8)]

    return curve, points


def test_weierstrass():
    for p in RANDOM_PRIMES:
        curve, points = make_weierstrass(p)

        results = echec.find_curves(points)
        assert len(results) == 1
        assert results[0] == curve


def test_weierstrass_known_prime():
    p = random.choice(echec.KNOWN_PRIMES)
    curve, points = make_weierstrass(p)

    results = echec.find_curves(points[:3])
    assert len(results) == 1
    assert results[0] == curve


def test_twisted_weierstrass():
    for p in RANDOM_PRIMES:
        curve, points = make_weierstrass(p, twist=True)

        results = echec.find_curves(points)
        assert len(results) == 1
        assert results[0] == curve


def test_twisted_weierstrass_known_prime():
    p = random.choice(echec.KNOWN_PRIMES)
    curve, points = make_weierstrass(p, twist=True)

    results = echec.find_curves(points[:4])
    assert len(results) == 1
    assert results[0] == curve


def test_not_enough_points():
    p = random.choice(echec.KNOWN_PRIMES)
    curve, points = make_weierstrass(p)

    results = echec.find_curves(points[:2])
    assert len(results) == 0


def make_montgomery(p):
    A = random.randint(1, p-1)
    B = random.randint(1, p-1)
    while B * (A**2 - 4) % p == 0:
        B = (B + 1) % p
    curve = montgomery.Montgomery(None, p, A, B)
    points = [random_point_on_curve(curve) for _ in range(8)]

    return curve, points


def test_montgomery():
    for p in RANDOM_PRIMES:
        curve, points = make_montgomery(p)

        results = echec.find_curves(points)
        assert len(results) == 1
        assert results[0] == curve


def test_montgomery_known_prime():
    p = random.choice(echec.KNOWN_PRIMES)
    curve, points = make_montgomery(p)

    results = echec.find_curves(points[:3])
    assert len(results) == 1
    assert results[0] == curve


def make_edwards(p):
    d = random.randint(2, p-1)
    t = random.randint(1, p-1)
    curve = edwards.Edwards(None, p, d, t)
    points = [random_point_on_curve(curve) for _ in range(8)]

    return curve, points


def test_edwards():
    for p in RANDOM_PRIMES:
        curve, points = make_edwards(p)

        results = echec.find_curves(points)
        assert len(results) == 1
        assert results[0] == curve


def test_edwards_known_prime():
    p = random.choice(echec.KNOWN_PRIMES)
    curve, points = make_edwards(p)

    results = echec.find_curves(points[:3])
    assert len(results) == 1
    assert results[0] == curve


def test_random_points():
    p = random.choice(echec.KNOWN_PRIMES)
    points = [random_point(p) for _ in range(8)]

    results = echec.find_curves(points)
    assert len(results) == 0
