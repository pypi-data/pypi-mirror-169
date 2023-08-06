from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class CalibrationPointRole(Enum):
    """
    The role of a calibration point in a log depth registration.

    :cvar LEFT_EDGE: Denotes the calibration being made on the left edge
        of the image.
    :cvar RIGHT_EDGE: Denotes the calibration being made on the right
        edge of the image.
    :cvar FRACTION: Denotes an intermediate point from the left edge to
        the right edge.
    :cvar OTHER: The value is not known. Avoid using this value. All
        reasonable attempts should be made to determine the appropriate
        value. Use of this value may result in rejection in some
        situations.
    """
    LEFT_EDGE = "left edge"
    RIGHT_EDGE = "right edge"
    FRACTION = "fraction"
    OTHER = "other"
