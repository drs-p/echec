
Echec - recognising elliptic curves
===================================

Echec is both a Python library and a command-line application for finding
elliptic curves over finite fields that contain one or more given points.
It implements two approaches to finding such curves:

*   First, it checks a list of known curves and returns any that contain all
    given points. In the case of point compression (i.e., when only the
    x-coordinates are known) it returns all known curves that contain all
    the given x-coordinates. Since, for every elliptic curve, about one-half
    of all possible x-values are a valid x-coordinate of a point on that curve,
    every input x-coordinate only gives a single bit of information,
    so there may be more than one matching curve.

*   Given a number of points that are all supposed to be on the same curve,
    it takes a number of elliptic curve formats and tries to compute the
    parameters of a matching curve. Currently supported elliptic curve formats
    are (short) Weierstrass, Montgomery and Edwards; quadratic twists of these
    are also supported. This approach generally requires that four or five
    points be given. Alternatively, the algorithm may assume that the
    characteristic of the underlying finite field is equal to that of one of
    the "known" curves; in that case, it can make do with one point less.

Currently, only elliptic curves over prime fields are implemented; extension
fields, including binary fields, are not (yet?) supported.


Installation
------------

Echec requires Python, version 3.8 or later.
It just *may* work against older versions (probably >= 3.6) as well, though this
is neither tested nor supported. Echec also requires SymPy.

The easiest way to install echec is to use pip to install either the source
distribution or the wheel:

    $ pip install echec-x.y.z.tar.gz

or

    $ pip install echec-x.y.z-py3-none-any.whl

If you want to install only the command-line tool, you can use pipx instead of
pip.


Usage
-----

### From the command line:

    echec <x> <y> [<x> <y> ...]
    echec --xcoords <x> [<x> ...]

        -x, --xcoords         all args are xcoords (point compression)


    $ echec 188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012 \
            07192b95ffc8da78631011ed6b24cdd573f977a11e794811

    Hits:
    nist/P-192: Weierstrass curve defined by
    y^2 = x^3 + -3*x + 2455155546008943817740293915197451784769108058161191238065
    over GF(6277101735386680763835789423207666416083908700390324961279)


    $ echec --xcoords \
            9 \
            e6db6867583030db3594c1a424b15f7c726624ec26b3353b10a903a6d0ab1c4c \
            c3da55379de9c6908e94ea4df28d084f32eccf03491c71f754b4075577a28552 \
            422c8e7a6227d7bca1350b3e2bb7279f7897b87bb6854b783c60e80311ae3079 \
            684cf59ba83309552800ef566f2f4d3c1c3887c49360e3875f2eb94d99532c51 \
            7c3911e0ab2586fd864497297e575e6f3bc601c0883c30df5f4dd2d24f665424 \
            8520f0098930a754748b7ddcb43ef75a0dbf3a0d26381af4eba4a98eaa9b4e6a \
            de9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f \
            4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742

    Hits:
    other/Curve25519: Montgomery curve defined by y^2 = x^3 + 486662*x^2 + x
    over GF(57896044618658097711785492504343953926634992332820282019728792003956564819949)


### From Python:

    >>> import echec.point
    >>> import echec.echec
    >>> points = [
    ...     echec.point.Point(
    ...         x="8BD2AEB9CB7E57CB2C4B482FFC81B7AFB9DE27E1E3BD23C23A4453BD9ACE3262",
    ...         y="547EF835C3DAC4FD97F8461A14611DC9C27745132DED8E545C1D54C72F046997",
    ...     )
    ... ]
    >>> [E.name for E in echec.echec.find_curves(points)]
    ['brainpool/brainpoolP256r1']

    >>> xcoords = [
    ...     "0x9",
    ...     "e6db6867583030db3594c1a424b15f7c726624ec26b3353b10a903a6d0ab1c4c",
    ...     "c3da55379de9c6908e94ea4df28d084f32eccf03491c71f754b4075577a28552",
    ...     "422c8e7a6227d7bca1350b3e2bb7279f7897b87bb6854b783c60e80311ae3079",
    ...     "684cf59ba83309552800ef566f2f4d3c1c3887c49360e3875f2eb94d99532c51",
    ...     "7c3911e0ab2586fd864497297e575e6f3bc601c0883c30df5f4dd2d24f665424",
    ...     "8520f0098930a754748b7ddcb43ef75a0dbf3a0d26381af4eba4a98eaa9b4e6a",
    ...     "de9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f",
    ...     "4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742",
    ...     "48d5ddd4061257ba166fa3f9bbdb74f1a4e81c089384fa77f790709f0dfbc766",
    ...     "0be7c1f5aad87d7e448662673298a443478b859745179eaf564c79c0ef6eee25",
    ...     "c74950607a12327f3204d94b6825bfb068b7f8319a9e3708ed3d43ce8130c950",
    ... ]
    >>> curves = echec.echec.find_curves_from_xcoords(xcoords)
    >>>> for curve in curves:
    ....     print(curve)

    other/Curve25519: Montgomery curve defined by y^2 = x^3 + 486662*x^2 + x
    over GF(57896044618658097711785492504343953926634992332820282019728792003956564819949)


Arguments, both to the command-line script and to the Python functions,
are (pairs of) decimal integers, hexadecimal integers (starting with "0x")
or strings of hexadecimal characters. Both big- and little-endian conversions
of these strings to integers are tried.
WARNING: command-line arguments like "00000010" will be interpreted as decimal
integers, not as hexadecimal!
