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
