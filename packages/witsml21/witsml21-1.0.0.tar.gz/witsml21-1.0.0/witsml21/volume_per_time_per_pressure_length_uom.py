from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerTimePerPressureLengthUom(Enum):
    """
    :cvar BBL_FT_PSI_D: barrel per day foot psi
    :cvar FT3_FT_PSI_D: cubic foot per day foot psi
    :cvar M2_K_PA_D: square metre per kilopascal day
    :cvar M2_PA_S: square metre per pascal second
    """
    BBL_FT_PSI_D = "bbl/(ft.psi.d)"
    FT3_FT_PSI_D = "ft3/(ft.psi.d)"
    M2_K_PA_D = "m2/(kPa.d)"
    M2_PA_S = "m2/(Pa.s)"
