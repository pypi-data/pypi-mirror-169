from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BladeShapeType(Enum):
    """
    Blade shape of the stabilizer: melon, spiral, straight, etc.
    """
    DYNAMIC = "dynamic"
    MELON = "melon"
    SPIRAL = "spiral"
    STRAIGHT = "straight"
    VARIABLE = "variable"
