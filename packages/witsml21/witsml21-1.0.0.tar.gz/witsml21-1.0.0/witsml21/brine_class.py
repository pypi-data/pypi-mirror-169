from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BrineType(Enum):
    """
    Specifies the class of brine.
    """
    CALCIUM_BROMIDE = "calcium bromide"
    POTASSIUM_BROMIDE = "potassium bromide"
    SODIUM_BROMIDE = "sodium bromide"
    ZINC_DIBROMIDE = "zinc dibromide"
    AMMONIUM_CHLORIDE = "ammonium chloride"
    CALCIUM_CHLORIDE = "calcium chloride"
    POTASSIUM_CHLORIDE = "potassium chloride"
    SODIUM_CHLORIDE = "sodium chloride"
    CESIUM_FORMATE = "cesium formate"
    POTASSIUM_FORMATE = "potassium formate"
    SODIUM_FORMATE = "sodium formate"
    BLEND = "blend"
