from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class LogSectionType(Enum):
    """
    Specifies the type of log section.

    :cvar MAIN:
    :cvar REPEAT: An interval of log that has been recorded for a second
        time.
    :cvar CALIBRATION:
    :cvar TIE_IN:
    :cvar GOING_IN_HOLE:
    :cvar OTHER: The value is not known. Avoid using this value. All
        reasonable attempts should be made to determine the appropriate
        value. Use of this value may result in rejection in some
        situations.
    """
    MAIN = "main"
    REPEAT = "repeat"
    CALIBRATION = "calibration"
    TIE_IN = "tie in"
    GOING_IN_HOLE = "going in hole"
    OTHER = "other"
