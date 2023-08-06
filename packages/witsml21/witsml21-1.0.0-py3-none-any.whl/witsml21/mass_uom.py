from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MassUom(Enum):
    """
    :cvar AG: attogram
    :cvar CG: centigram
    :cvar CT: carat
    :cvar CWT_UK: UK hundredweight
    :cvar CWT_US: US hundredweight
    :cvar EG: exagram
    :cvar FG: femtogram
    :cvar G: gram
    :cvar GG: gigagram
    :cvar GRAIN: grain
    :cvar HG: hectogram
    :cvar KG: kilogram
    :cvar KLBM: thousand pound-mass
    :cvar LBM: pound-mass
    :cvar MG: milligram
    :cvar MG_1: megagram
    :cvar NG: nanogram
    :cvar OZM: ounce-mass
    :cvar OZM_TROY: troy ounce-mass
    :cvar PG: picogram
    :cvar SACK_94LBM: 94 pound-mass sack
    :cvar T: tonne
    :cvar TG: teragram
    :cvar TON_UK: UK ton-mass
    :cvar TON_US: US ton-mass
    :cvar UG: microgram
    """
    AG = "ag"
    CG = "cg"
    CT = "ct"
    CWT_UK = "cwt[UK]"
    CWT_US = "cwt[US]"
    EG = "Eg"
    FG = "fg"
    G = "g"
    GG = "Gg"
    GRAIN = "grain"
    HG = "hg"
    KG = "kg"
    KLBM = "klbm"
    LBM = "lbm"
    MG = "mg"
    MG_1 = "Mg"
    NG = "ng"
    OZM = "ozm"
    OZM_TROY = "ozm[troy]"
    PG = "pg"
    SACK_94LBM = "sack[94lbm]"
    T = "t"
    TG = "Tg"
    TON_UK = "ton[UK]"
    TON_US = "ton[US]"
    UG = "ug"
