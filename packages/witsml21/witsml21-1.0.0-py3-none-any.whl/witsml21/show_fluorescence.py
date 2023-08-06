from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ShowFluorescence(Enum):
    """
    Specifies the intensity and color of the show.
    """
    FAINT = "faint"
    BRIGHT = "bright"
    NONE = "none"
