from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class TimePerLengthUom(Enum):
    """
    :cvar VALUE_0_001_H_FT: hour per thousand foot
    :cvar H_KM: hour per kilometre
    :cvar MIN_FT: minute per foot
    :cvar MIN_M: minute per metre
    :cvar MS_CM: millisecond per centimetre
    :cvar MS_FT: millisecond per foot
    :cvar MS_IN: millisecond per inch
    :cvar MS_M: millisecond per metre
    :cvar NS_FT: nanosecond per foot
    :cvar NS_M: nanosecond per metre
    :cvar S_CM: second per centimetre
    :cvar S_FT: second per foot
    :cvar S_IN: second per inch
    :cvar S_M: second per metre
    :cvar US_FT: microsecond per foot
    :cvar US_IN: microsecond per inch
    :cvar US_M: microsecond per metre
    """
    VALUE_0_001_H_FT = "0.001 h/ft"
    H_KM = "h/km"
    MIN_FT = "min/ft"
    MIN_M = "min/m"
    MS_CM = "ms/cm"
    MS_FT = "ms/ft"
    MS_IN = "ms/in"
    MS_M = "ms/m"
    NS_FT = "ns/ft"
    NS_M = "ns/m"
    S_CM = "s/cm"
    S_FT = "s/ft"
    S_IN = "s/in"
    S_M = "s/m"
    US_FT = "us/ft"
    US_IN = "us/in"
    US_M = "us/m"
