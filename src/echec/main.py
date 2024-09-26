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


import sys

from . import echec, point, options


def main():
    optspec = """
echec <x> <y> [<x> <y> ...]
echec --xcoords <x> [<x> ...]
--
x,xcoords   all args are xcoords (point compression)
"""
    optparser = options.Options(optspec)
    opt, flags, args = optparser.parse(sys.argv[1:])

    if opt.xcoords is None:
        if not args or len(args) % 2 != 0:
            optparser.usage()

        points = []
        while args:
            x, y, *args = args
            points.append(point.Point(x,y))

        curves = echec.find_curves(points)
    else:
        curves = echec.find_curves_from_xcoords(args)

    if curves:
        print("Hits:")
        for curve in curves:
            print(curve)
        return 0
    else:
        print("No curves found")
        return 1
