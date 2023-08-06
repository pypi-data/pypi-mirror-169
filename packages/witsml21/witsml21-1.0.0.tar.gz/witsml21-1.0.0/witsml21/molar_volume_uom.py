from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MolarVolumeUom(Enum):
    """
    :cvar DM3_KMOL: cubic decimetre per kilogram-mole
    :cvar FT3_LBMOL: cubic foot per pound-mass-mole
    :cvar L_KMOL: litre per kilogram-mole
    :cvar L_MOL: litre per gram-mole
    :cvar M3_KMOL: cubic metre per kilogram-mole
    :cvar M3_MOL: cubic metre per gram-mole
    """
    DM3_KMOL = "dm3/kmol"
    FT3_LBMOL = "ft3/lbmol"
    L_KMOL = "L/kmol"
    L_MOL = "L/mol"
    M3_KMOL = "m3/kmol"
    M3_MOL = "m3/mol"
