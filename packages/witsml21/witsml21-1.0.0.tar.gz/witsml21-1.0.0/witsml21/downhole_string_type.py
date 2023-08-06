from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class DownholeStringType(Enum):
    """
    Specifies the values for the type of downhole strings.
    """
    CASING = "casing"
    OTHERS = "others"
    ROD = "rod"
    TUBING = "tubing"
    WELLHEAD = "wellhead"
