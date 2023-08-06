from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MassPerTimePerAreaUom(Enum):
    """
    :cvar G_FT_CM3_S: gram foot per cubic centimetre second
    :cvar G_M_CM3_S: gram metre per cubic centimetre second
    :cvar KG_M2_S: kilogram per square metre second
    :cvar K_PA_S_M: kilopascal second per metre
    :cvar LBM_FT2_H: pound-mass per square foot hour
    :cvar LBM_FT2_S: pound-mass per square foot second
    :cvar MPA_S_M: megapascal second per metre
    """
    G_FT_CM3_S = "g.ft/(cm3.s)"
    G_M_CM3_S = "g.m/(cm3.s)"
    KG_M2_S = "kg/(m2.s)"
    K_PA_S_M = "kPa.s/m"
    LBM_FT2_H = "lbm/(ft2.h)"
    LBM_FT2_S = "lbm/(ft2.s)"
    MPA_S_M = "MPa.s/m"
