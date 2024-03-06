"""
evermore: Differentiable (binned) likelihoods in JAX.
"""
from __future__ import annotations

__author__ = "Peter Fackeldey"
__email__ = "peter.fackeldey@rwth-aachen.de"
__copyright__ = "Copyright 2023, Peter Fackeldey"
__credits__ = ["Peter Fackeldey"]
__contact__ = "https://github.com/pfackeldey/evermore"
__license__ = "BSD-3-Clause"
__status__ = "Development"
__version__ = "0.2.0"


# expose public API

__all__ = [
    "__version__",
    "effect",
    "loss",
    "pdf",
    "util",
    "sample",
    # explicitely expose some classes
    "Parameter",
    "modifier",
    # "staterror",
    # "autostaterrors",
    "compose",
]


def __dir__():
    return __all__


from evermore import (  # noqa: E402
    effect,
    loss,
    pdf,
    sample,
    util,
)

# from evermore.model import Model, Result
from evermore.modifier import (  # noqa: E402
    # autostaterrors,
    compose,
    modifier,
)

# staterror,
from evermore.parameter import Parameter  # noqa: E402
