from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class TargetSectionScope(Enum):
    """
    These values represent the type of scope of a section that describes a
    target.

    :cvar ARC: continuous curve
    :cvar LINE: straight line
    """
    ARC = "arc"
    LINE = "line"
