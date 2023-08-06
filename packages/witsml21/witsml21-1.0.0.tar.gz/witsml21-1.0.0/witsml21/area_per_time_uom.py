from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AreaPerTimeUom(Enum):
    """
    :cvar CM2_S: square centimetre per second
    :cvar FT2_H: square foot per hour
    :cvar FT2_S: square foot per second
    :cvar IN2_S: square inch per second
    :cvar M2_D: square metre per day
    :cvar M2_H: square metre per hour
    :cvar M2_S: square metre per second
    :cvar MM2_S: square millimetre per second
    """
    CM2_S = "cm2/s"
    FT2_H = "ft2/h"
    FT2_S = "ft2/s"
    IN2_S = "in2/s"
    M2_D = "m2/d"
    M2_H = "m2/h"
    M2_S = "m2/s"
    MM2_S = "mm2/s"
