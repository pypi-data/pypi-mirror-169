from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AreaPerAreaUom(Enum):
    """
    :cvar VALUE: percent
    :cvar AREA: percent [area basis]
    :cvar C_EUC: centieuclid
    :cvar EUC: euclid
    :cvar IN2_FT2: square inch per square foot
    :cvar IN2_IN2: square inch per square inch
    :cvar M2_M2: square metre per square metre
    :cvar MM2_MM2: square millimetre per square millimetre
    """
    VALUE = "%"
    AREA = "%[area]"
    C_EUC = "cEuc"
    EUC = "Euc"
    IN2_FT2 = "in2/ft2"
    IN2_IN2 = "in2/in2"
    M2_M2 = "m2/m2"
    MM2_MM2 = "mm2/mm2"
