from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ForcePerForceUom(Enum):
    """
    :cvar VALUE: percent
    :cvar EUC: euclid
    :cvar KGF_KGF: thousand gram-force per kilogram-force
    :cvar LBF_LBF: pound-force per pound-force
    :cvar N_N: newton per newton
    """
    VALUE = "%"
    EUC = "Euc"
    KGF_KGF = "kgf/kgf"
    LBF_LBF = "lbf/lbf"
    N_N = "N/N"
