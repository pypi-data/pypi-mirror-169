from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PpfgtectonicSetting(Enum):
    """
    Specifies the source of PPFG data.
    """
    COMPRESSIONAL = "compressional"
    EXTENSIONAL = "extensional"
    STRIKE_SLIP = "strike slip"
    TRANSPRESSIONAL = "transpressional"
    TRANSTENSIONAL = "transtensional"
