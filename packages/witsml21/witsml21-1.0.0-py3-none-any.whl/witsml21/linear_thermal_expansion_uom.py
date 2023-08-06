from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LinearThermalExpansionUom(Enum):
    """
    :cvar VALUE_1_DELTA_K: per delta kelvin
    :cvar IN_IN_DELTA_F: inch per inch delta Fahrenheit
    :cvar M_M_DELTA_K: metre per metre delta kelvin
    :cvar MM_MM_DELTA_K: millimetre per millimetre delta kelvin
    """
    VALUE_1_DELTA_K = "1/deltaK"
    IN_IN_DELTA_F = "in/(in.deltaF)"
    M_M_DELTA_K = "m/(m.deltaK)"
    MM_MM_DELTA_K = "mm/(mm.deltaK)"
