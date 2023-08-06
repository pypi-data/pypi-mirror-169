from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class TargetCategory(Enum):
    """
    :cvar GEOLOGICAL:
    :cvar WELL_CONTROL: A target being used for well control in another
        wellbore. This is drilled in the first step of a dynamic kill
        operation.
    """
    GEOLOGICAL = "geological"
    WELL_CONTROL = "well control"
