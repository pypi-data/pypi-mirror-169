from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StratigraphyKind(Enum):
    BIOSTRATIGRAPHIC = "biostratigraphic"
    CHEMOSTRATIGRAPHIC = "chemostratigraphic"
    CHRONOSTRATIGRAPHIC = "chronostratigraphic"
    FLUID_STRATIGRAPHIC = "fluid stratigraphic"
    LITHOSTRATIGRAPHIC = "lithostratigraphic"
    MAGNETOSTRATIGRAPHIC = "magnetostratigraphic"
    SEISMIC_STRATIGRAPHIC = "seismic stratigraphic"
    SEQUENCE_STRATIGRAPHIC = "sequence stratigraphic"
