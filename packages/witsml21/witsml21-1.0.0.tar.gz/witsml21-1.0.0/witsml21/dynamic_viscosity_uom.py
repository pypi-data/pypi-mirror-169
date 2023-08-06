from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class DynamicViscosityUom(Enum):
    """
    :cvar C_P: centipoise
    :cvar D_P: decipoise
    :cvar DYNE_S_CM2: dyne second per square centimetre
    :cvar EP: exapoise
    :cvar F_P: femtopoise
    :cvar GP: gigapoise
    :cvar KGF_S_M2: thousand gram-force second per square metre
    :cvar K_P: kilopoise
    :cvar LBF_S_FT2: pound-force second per square foot
    :cvar LBF_S_IN2: pound-force second per square inch
    :cvar M_P: millipoise
    :cvar MP_1: megapoise
    :cvar M_PA_S: millipascal second
    :cvar N_S_M2: newton second per square metre
    :cvar N_P: nanopoise
    :cvar P: poise
    :cvar PA_S: pascal second
    :cvar P_P: picopoise
    :cvar PSI_S: psi second
    :cvar TP: terapoise
    :cvar U_P: micropoise
    """
    C_P = "cP"
    D_P = "dP"
    DYNE_S_CM2 = "dyne.s/cm2"
    EP = "EP"
    F_P = "fP"
    GP = "GP"
    KGF_S_M2 = "kgf.s/m2"
    K_P = "kP"
    LBF_S_FT2 = "lbf.s/ft2"
    LBF_S_IN2 = "lbf.s/in2"
    M_P = "mP"
    MP_1 = "MP"
    M_PA_S = "mPa.s"
    N_S_M2 = "N.s/m2"
    N_P = "nP"
    P = "P"
    PA_S = "Pa.s"
    P_P = "pP"
    PSI_S = "psi.s"
    TP = "TP"
    U_P = "uP"
