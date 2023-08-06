from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class HeatTransferCoefficientUom(Enum):
    """
    :cvar BTU_IT_H_FT2_DELTA_F: BTU per hour square foot delta
        Fahrenheit
    :cvar BTU_IT_H_FT2_DELTA_R: BTU per hour square foot delta Rankine
    :cvar BTU_IT_H_M2_DELTA_C: BTU per hour square metre delta Celsius
    :cvar BTU_IT_S_FT2_DELTA_F: (BTU per second) per square foot delta
        Fahrenheit
    :cvar CAL_TH_H_CM2_DELTA_C: calorie per hour square centimetre delta
        Celsius
    :cvar CAL_TH_S_CM2_DELTA_C: calorie per second square centimetre
        delta Celsius
    :cvar J_S_M2_DELTA_C: joule per second square metre delta Celsius
    :cvar KCAL_TH_H_M2_DELTA_C: thousand calorie per hour square metre
        delta Celsius
    :cvar K_J_H_M2_DELTA_K: kilojoule per hour square metre delta kelvin
    :cvar K_W_M2_DELTA_K: kilowatt per square metre delta kelvin
    :cvar W_M2_DELTA_K: watt per square metre delta kelvin
    """
    BTU_IT_H_FT2_DELTA_F = "Btu[IT]/(h.ft2.deltaF)"
    BTU_IT_H_FT2_DELTA_R = "Btu[IT]/(h.ft2.deltaR)"
    BTU_IT_H_M2_DELTA_C = "Btu[IT]/(h.m2.deltaC)"
    BTU_IT_S_FT2_DELTA_F = "Btu[IT]/(s.ft2.deltaF)"
    CAL_TH_H_CM2_DELTA_C = "cal[th]/(h.cm2.deltaC)"
    CAL_TH_S_CM2_DELTA_C = "cal[th]/(s.cm2.deltaC)"
    J_S_M2_DELTA_C = "J/(s.m2.deltaC)"
    KCAL_TH_H_M2_DELTA_C = "kcal[th]/(h.m2.deltaC)"
    K_J_H_M2_DELTA_K = "kJ/(h.m2.deltaK)"
    K_W_M2_DELTA_K = "kW/(m2.deltaK)"
    W_M2_DELTA_K = "W/(m2.deltaK)"
