from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellboreShape(Enum):
    """Specifies values to represent the classification of a wellbore based on
    its shape.

    The source of the values and the descriptions is the POSC V2.2
    "facility class" standard instance values in classification system
    "POSC wellbore trajectory shape".

    :cvar BUILD_AND_HOLD: A wellbore configuration where the inclination
        is increased to some terminal angle of inclination and
        maintained at that angle to the specified target.
    :cvar DEVIATED: A wellbore that significantly departs from vertical
        with respect to the surface location.
    :cvar DOUBLE_KICKOFF: Incorporates two tangential (constant, non-
        zero inclination) sections, the second of which must be at a
        higher inclination than the first.
    :cvar HORIZONTAL: A wellbore whose path deviates from the vertical
        by at least 75 degrees.
    :cvar S_SHAPED: A wellbore drilled with a vertical segment, a
        deviated segment, and a return toward a vertical segment.
    :cvar VERTICAL: A wellbore that is nearly vertical with respect to
        the surface location.
    """
    BUILD_AND_HOLD = "build and hold"
    DEVIATED = "deviated"
    DOUBLE_KICKOFF = "double kickoff"
    HORIZONTAL = "horizontal"
    S_SHAPED = "S-shaped"
    VERTICAL = "vertical"
