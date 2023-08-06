from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ForcePerLengthUom(Enum):
    """
    :cvar VALUE_0_01_LBF_FT: pound-force per hundred foot
    :cvar VALUE_1_30_LBF_M: pound-force per thirty metre
    :cvar VALUE_1_30_N_M: newton per thirty metre
    :cvar DYNE_CM: dyne per centimetre
    :cvar KGF_CM: thousand gram-force per centimetre
    :cvar K_N_M: kilonewton per metre
    :cvar LBF_FT: pound-force per foot
    :cvar LBF_IN: pound-force per inch
    :cvar M_N_KM: millinewton per kilometre
    :cvar M_N_M: millinewton per metre
    :cvar N_M: newton per metre
    :cvar PDL_CM: poundal per centimetre
    :cvar TONF_UK_FT: UK ton-force per foot
    :cvar TONF_US_FT: US ton-force per foot
    """
    VALUE_0_01_LBF_FT = "0.01 lbf/ft"
    VALUE_1_30_LBF_M = "1/30 lbf/m"
    VALUE_1_30_N_M = "1/30 N/m"
    DYNE_CM = "dyne/cm"
    KGF_CM = "kgf/cm"
    K_N_M = "kN/m"
    LBF_FT = "lbf/ft"
    LBF_IN = "lbf/in"
    M_N_KM = "mN/km"
    M_N_M = "mN/m"
    N_M = "N/m"
    PDL_CM = "pdl/cm"
    TONF_UK_FT = "tonf[UK]/ft"
    TONF_US_FT = "tonf[US]/ft"
