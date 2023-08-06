from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StimMaterialKind(Enum):
    """
    Specifies the type of stimulation material.
    """
    ADDITIVE = "additive"
    BRINE = "brine"
    CO2 = "CO2"
    GEL = "gel"
    N2 = "N2"
    OTHER = "other"
    PROPPANT_AGENT = "proppant agent"
    WATER = "water"
