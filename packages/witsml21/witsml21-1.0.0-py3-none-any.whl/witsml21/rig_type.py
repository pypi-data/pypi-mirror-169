from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class RigType(Enum):
    """
    Specifies the type of drilling rig.

    :cvar BARGE: Barge rig.
    :cvar COILED_TUBING: Coiled tubing rig.
    :cvar FLOATER: Floating rig.
    :cvar JACKUP: Jackup rig.
    :cvar LAND: Land rig.
    :cvar PLATFORM: Fixed platform.
    :cvar SEMI_SUBMERSIBLE: Semi-submersible rig.
    """
    BARGE = "barge"
    COILED_TUBING = "coiled tubing"
    FLOATER = "floater"
    JACKUP = "jackup"
    LAND = "land"
    PLATFORM = "platform"
    SEMI_SUBMERSIBLE = "semi-submersible"
