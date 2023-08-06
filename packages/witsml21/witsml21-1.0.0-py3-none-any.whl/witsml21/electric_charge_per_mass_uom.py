from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ElectricChargePerMassUom(Enum):
    """
    :cvar A_S_KG: ampere second per kilogram
    :cvar C_G: coulomb per gram
    :cvar C_KG: coulomb per kilogram
    """
    A_S_KG = "A.s/kg"
    C_G = "C/g"
    C_KG = "C/kg"
