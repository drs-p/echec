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


from gmpy2 import mpz


__all__ = ["from_bytes", "to_bytes", "to_integer", "byteswap"]


try:
    from_bytes = mpz.from_bytes
except AttributeError:
    def from_bytes(s, byteorder="big", signed=False):
        return mpz(int.from_bytes(s, byteorder=byteorder, signed=signed))

try:
    to_bytes = mpz.to_bytes
except AttributeError:
    def to_bytes(n, length=1, byteorder='big', *, signed=False):
        return int(n).to_bytes(length=length, byteorder=byteorder, signed=signed)


def to_integer(x):
    try:
        x = mpz(x)
    except ValueError:
        x = mpz(x, 16)

    return x


def byteswap(x):
    nbytes_x = (x.bit_length() + 7) // 8

    return from_bytes(to_bytes(x, length=nbytes_x, byteorder="big"),
                      byteorder="little")
