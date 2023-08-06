from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PassDirection(Enum):
    """
    :cvar UP: The tool is moving up (decreasing depth).
    :cvar HOLDING_STEADY: The tools is not moving up or down (depth is
        not changing).
    :cvar DOWN: The tool is moving down (increasing depth).
    """
    UP = "up"
    HOLDING_STEADY = "holding steady"
    DOWN = "down"
