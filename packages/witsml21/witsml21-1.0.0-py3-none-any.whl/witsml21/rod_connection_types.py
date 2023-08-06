from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class RodConnectionTypes(Enum):
    """
    Specifies the values for the connection type of rod.
    """
    EATING_NIPPLE_CUP = "eating nipple-cup"
    LATCHED = "latched"
    SEATING_NIPPLE_MECHANICAL = "seating nipple-mechanical"
    SLIPFIT_SEALED = "slipfit sealed"
    THREADED = "threaded"
    WELDED = "welded"
