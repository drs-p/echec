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


from .helpers import to_integer, byteswap


class Point:
    def __init__(self, x, y):
        self.x = to_integer(x)
        self.y = to_integer(y)

    def __repr__(self):
        return f"{self.__class__}({self.__dict__})"

    def byteswapped(self):
        return self.__class__(byteswap(self.x), byteswap(self.y))
