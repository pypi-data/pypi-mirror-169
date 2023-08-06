from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AmountOfSubstancePerAmountOfSubstanceUom(Enum):
    """
    :cvar VALUE: percent
    :cvar MOLAR: percent [molar basis]
    :cvar EUC: euclid
    :cvar MOL_MOL: mole per mole
    :cvar N_EUC: nanoeuclid
    :cvar PPK: part per thousand
    :cvar PPM: part per million
    """
    VALUE = "%"
    MOLAR = "%[molar]"
    EUC = "Euc"
    MOL_MOL = "mol/mol"
    N_EUC = "nEuc"
    PPK = "ppk"
    PPM = "ppm"
