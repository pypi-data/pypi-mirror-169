from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellboreMarkerKind(Enum):
    POINT_OF_INTEREST = "point of interest"
    STRATIGRAPHIC = "stratigraphic"
