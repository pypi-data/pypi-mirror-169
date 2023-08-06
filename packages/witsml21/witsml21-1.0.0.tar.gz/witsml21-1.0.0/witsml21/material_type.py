from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class MaterialType(Enum):
    """
    Specifies the primary type of material that a component is made of.
    """
    ALUMINUM = "aluminum"
    BERYLLIUM_COPPER = "beryllium copper"
    CHROME_ALLOY = "chrome alloy"
    COMPOSITE = "composite"
    OTHER = "other"
    NON_MAGNETIC_STEEL = "non-magnetic steel"
    PLASTIC = "plastic"
    STEEL = "steel"
    STEEL_ALLOY = "steel alloy"
    TITANIUM = "titanium"
