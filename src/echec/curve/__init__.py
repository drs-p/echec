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


import importlib
import pathlib
import sys

# Import all packages in this module without naming them explicitly
location = pathlib.Path(__file__).parent
__all__ = [fn.stem for fn in location.glob("[a-z]*.py")]
ns = sys.modules[__name__].__dict__
for m in __all__:
    # Relative imports need a leading dot (see docs)
    ns[m] = importlib.import_module("." + m, __package__)


# Create a list of all currently implemented types of elliptic curves.
CURVE_TYPES = [cls for m in __all__ for cls in ns[m].__dict__.values()
               if type(cls).__name__ == "type"
                    and issubclass(cls, abstractcurve.AbstractCurve)
                    and cls != abstractcurve.AbstractCurve]
