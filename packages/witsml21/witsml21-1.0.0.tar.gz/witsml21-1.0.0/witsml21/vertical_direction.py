from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VerticalDirection(Enum):
    """
    :cvar UP: Values are positive when moving away from the center of
        the Earth.
    :cvar DOWN: Values are positive when moving toward the center of the
        Earth.
    """
    UP = "up"
    DOWN = "down"
