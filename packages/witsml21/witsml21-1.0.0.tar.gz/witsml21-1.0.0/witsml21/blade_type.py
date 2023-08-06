from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BladeType(Enum):
    """
    Specifies the blade type of the stabilizer.
    """
    CLAMP_ON = "clamp-on"
    INTEGRAL = "integral"
    SLEEVE = "sleeve"
    WELDED = "welded"
