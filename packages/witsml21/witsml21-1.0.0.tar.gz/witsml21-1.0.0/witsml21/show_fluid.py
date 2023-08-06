from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ShowFluid(Enum):
    """
    Specifies the type of fluid analyzed in this interval.
    """
    GAS = "gas"
    OIL = "oil"
