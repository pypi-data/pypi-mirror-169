from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StimFluidKind(Enum):
    """
    Specifies the fluid type.

    :cvar ACID_BASED: A fluid in which the primary fluid medium of
        mixing and transport is acidic (substance which reacts with a
        base; aqueous acids have a pH less than 7).
    :cvar GAS: A carrier medium in which gas is the primary medium of
        mixing and transport.
    :cvar OIL_BASED: A fluid in which oil is the primary fluid medium of
        mixing and transport.
    :cvar WATER_BASED:
    """
    ACID_BASED = "acid-based"
    GAS = "gas"
    OIL_BASED = "oil-based"
    WATER_BASED = "water-based"
