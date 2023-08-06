from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class EnergyPerLengthUom(Enum):
    """
    :cvar J_M: joule per metre
    :cvar MJ_M: megajoule per metre
    """
    J_M = "J/m"
    MJ_M = "MJ/m"
