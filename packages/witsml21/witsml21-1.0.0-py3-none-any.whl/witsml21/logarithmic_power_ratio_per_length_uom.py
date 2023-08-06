from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LogarithmicPowerRatioPerLengthUom(Enum):
    """
    :cvar B_M: bel per metre
    :cvar D_B_FT: decibel per foot
    :cvar D_B_KM: decibel per kilometre
    :cvar D_B_M: decibel per metre
    """
    B_M = "B/m"
    D_B_FT = "dB/ft"
    D_B_KM = "dB/km"
    D_B_M = "dB/m"
