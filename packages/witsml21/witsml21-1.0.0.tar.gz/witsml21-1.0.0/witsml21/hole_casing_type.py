from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class HoleCasingType(Enum):
    """
    Specifies values for the types of hole casing.
    """
    BLOW_OUT_PREVENTER = "blow out preventer"
    CASING = "casing"
    CONDUCTOR = "conductor"
    CURVED_CONDUCTOR = "curved conductor"
    LINER = "liner"
    OPEN_HOLE = "open hole"
    RISER = "riser"
    TUBING = "tubing"
