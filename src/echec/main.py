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
