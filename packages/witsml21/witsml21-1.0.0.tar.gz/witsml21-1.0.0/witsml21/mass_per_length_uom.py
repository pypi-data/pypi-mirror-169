from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MassPerLengthUom(Enum):
    """
    :cvar KG_M_CM2: kilogram metre per square centimetre
    :cvar KG_M: kilogram per metre
    :cvar KLBM_IN: thousand pound-mass per inch
    :cvar LBM_FT: pound-mass per foot
    :cvar MG_IN: megagram per inch
    """
    KG_M_CM2 = "kg.m/cm2"
    KG_M = "kg/m"
    KLBM_IN = "klbm/in"
    LBM_FT = "lbm/ft"
    MG_IN = "Mg/in"
