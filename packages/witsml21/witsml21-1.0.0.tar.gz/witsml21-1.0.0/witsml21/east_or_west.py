from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class EastOrWest(Enum):
    """
    Specifies east or west direction.

    :cvar EAST: East of something.
    :cvar WEST: West of something.
    """
    EAST = "east"
    WEST = "west"
