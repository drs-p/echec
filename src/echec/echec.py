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


from .curve import CURVE_TYPES
from .helpers import to_integer, byteswap
from .known_curves import KNOWN_CURVES, KNOWN_PRIMES


def find_curves(points):
    """
    Find elliptic curves that contain all given points.

    The coordinates of the points may be either integers or hex strings.
    In all cases, the coordinates are tried both "as-is"
    and with byte-order swapped.
    """
    swapped = [q.byteswapped() for q in points]

    return sorted(list(frozenset(
            _find_known_curves(points)
                + _find_known_curves(swapped)
            or _find_unknown_curves(points, primes=KNOWN_PRIMES)
                + _find_unknown_curves(swapped, primes=KNOWN_PRIMES)
        )), key=lambda curve: curve.name)


def _find_known_curves(points):
    """
    Find all known curves that contain all given points.
    """
    if len(points) == 0:
        return []
    else:
        return [curve for curve in KNOWN_CURVES
                if all(curve.contains_point(q) for q in points)]


def _find_unknown_curves(points, primes=None):
    """
    Find the parameters of one or more curves (of the types
    in CURVE_TYPES) that contain all given points.

    The parameter `primes` contains an optional list of primes
    that may be used as the characteristic of the finite field
    over which the curve is defined. Specifying this parameter
    *may* allow the implementation to succeed with fewer input
    points than would otherwise be required.
    """
    if len(points) == 0:
        return []
    else:
        curves = [curve_class.find_curve_from_points(*points, primes=primes)
                  for curve_class in CURVE_TYPES]
        return [curve for curve in curves if curve is not None]


def find_curves_from_xcoords(xcoords):
    """
    Return all known curves that contain all given x-coordinates.

    Each x-coordinate may be either an integer or a hexadecimal string.
    In all cases, the coordinates are tried both "as-is"
    and with byte-order swapped.
    """
    xcoords = [to_integer(x) for x in xcoords]
    swapped = [byteswap(x) for x in xcoords]

    results = []
    for curve in KNOWN_CURVES:
        if all(curve.contains_xcoord(x) for x in xcoords) \
        or all(curve.contains_xcoord(x) for x in swapped):
            results.append(curve)

    return results
