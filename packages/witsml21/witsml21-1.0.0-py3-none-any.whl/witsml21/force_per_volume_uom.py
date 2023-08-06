from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ForcePerVolumeUom(Enum):
    """
    :cvar VALUE_0_001_PSI_FT: psi per thousand foot
    :cvar VALUE_0_01_PSI_FT: psi per hundred foot
    :cvar ATM_FT: standard atmosphere per foot
    :cvar ATM_HM: standard atmosphere per hundred metre
    :cvar ATM_M: standard atmosphere per metre
    :cvar BAR_KM: bar per kilometre
    :cvar BAR_M: bar per metre
    :cvar GPA_CM: gigapascal per centimetre
    :cvar K_PA_HM: kilopascal per hectometre
    :cvar K_PA_M: kilopascal per metre
    :cvar LBF_FT3: pound-force per cubic foot
    :cvar LBF_GAL_US: pound-force per US gallon
    :cvar MPA_M: megapascal per metre
    :cvar N_M3: newton per cubic metre
    :cvar PA_M: pascal per metre
    :cvar PSI_FT: psi per foot
    :cvar PSI_M: psi per metre
    """
    VALUE_0_001_PSI_FT = "0.001 psi/ft"
    VALUE_0_01_PSI_FT = "0.01 psi/ft"
    ATM_FT = "atm/ft"
    ATM_HM = "atm/hm"
    ATM_M = "atm/m"
    BAR_KM = "bar/km"
    BAR_M = "bar/m"
    GPA_CM = "GPa/cm"
    K_PA_HM = "kPa/hm"
    K_PA_M = "kPa/m"
    LBF_FT3 = "lbf/ft3"
    LBF_GAL_US = "lbf/gal[US]"
    MPA_M = "MPa/m"
    N_M3 = "N/m3"
    PA_M = "Pa/m"
    PSI_FT = "psi/ft"
    PSI_M = "psi/m"
