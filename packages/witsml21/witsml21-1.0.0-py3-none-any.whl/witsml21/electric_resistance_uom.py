from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ElectricResistanceUom(Enum):
    """
    :cvar COHM: centiohm
    :cvar DOHM: deciohm
    :cvar EOHM: exaohm
    :cvar FOHM: femtoohm
    :cvar GOHM: gigaohm
    :cvar KOHM: kilohm
    :cvar MOHM: megohm
    :cvar MOHM_1: milliohm
    :cvar NOHM: nanoohm
    :cvar OHM: ohm
    :cvar POHM: picoohm
    :cvar TOHM: teraohm
    :cvar UOHM: microohm
    """
    COHM = "cohm"
    DOHM = "dohm"
    EOHM = "Eohm"
    FOHM = "fohm"
    GOHM = "Gohm"
    KOHM = "kohm"
    MOHM = "Mohm"
    MOHM_1 = "mohm"
    NOHM = "nohm"
    OHM = "ohm"
    POHM = "pohm"
    TOHM = "Tohm"
    UOHM = "uohm"
