from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class EnergyLengthPerTimeAreaTemperatureUom(Enum):
    """
    :cvar BTU_IT_IN_H_FT2_DELTA_F: BTU per (hour square foot delta
        Fahrenheit per inch)
    :cvar J_M_S_M2_DELTA_K: joule metre per second square metre delta
        kelvin
    :cvar K_J_M_H_M2_DELTA_K: kilojoule metre per hour square metre
        delta kelvin
    :cvar W_M_DELTA_K: watt per metre delta kelvin
    """
    BTU_IT_IN_H_FT2_DELTA_F = "Btu[IT].in/(h.ft2.deltaF)"
    J_M_S_M2_DELTA_K = "J.m/(s.m2.deltaK)"
    K_J_M_H_M2_DELTA_K = "kJ.m/(h.m2.deltaK)"
    W_M_DELTA_K = "W/(m.deltaK)"
