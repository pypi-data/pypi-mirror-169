from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ElectricConductanceUom(Enum):
    """
    :cvar C_S: centisiemens
    :cvar D_S: decisiemens
    :cvar ES: exasiemens
    :cvar F_S: femtosiemens
    :cvar GS: gigasiemens
    :cvar K_S: kilosiemens
    :cvar M_S: millisiemens
    :cvar MS_1: megasiemens
    :cvar N_S: nanosiemens
    :cvar P_S: picosiemens
    :cvar S: siemens
    :cvar TS: terasiemens
    :cvar U_S: microsiemens
    """
    C_S = "cS"
    D_S = "dS"
    ES = "ES"
    F_S = "fS"
    GS = "GS"
    K_S = "kS"
    M_S = "mS"
    MS_1 = "MS"
    N_S = "nS"
    P_S = "pS"
    S = "S"
    TS = "TS"
    U_S = "uS"
