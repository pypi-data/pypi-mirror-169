from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class MudType(Enum):
    """
    Specifies the class of a drilling fluid.

    :cvar OIL_BASED:
    :cvar WATER_BASED:
    :cvar OTHER: A drilling fluid in which neither water nor oil is the
        continuous phase.
    :cvar PNEUMATIC: A drilling fluid which is gas-based.
    """
    OIL_BASED = "oil-based"
    WATER_BASED = "water-based"
    OTHER = "other"
    PNEUMATIC = "pneumatic"
