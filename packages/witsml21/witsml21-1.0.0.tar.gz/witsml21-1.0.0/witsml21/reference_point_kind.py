from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReferencePointKind(Enum):
    """
    This enumeration holds the normal wellbore datum references plus Well head
    and well surface location, the two common reference points not along a
    wellbore.
    """
    CASING_FLANGE = "casing flange"
    CROWN_VALVE = "crown valve"
    DERRICK_FLOOR = "derrick floor"
    GROUND_LEVEL = "ground level"
    KELLY_BUSHING = "kelly bushing"
    KICKOFF_POINT = "kickoff point"
    LOWEST_ASTRONOMICAL_TIDE = "lowest astronomical tide"
    MEAN_HIGH_WATER = "mean high water"
    MEAN_HIGHER_HIGH_WATER = "mean higher high water"
    MEAN_LOW_WATER = "mean low water"
    MEAN_LOWER_LOW_WATER = "mean lower low water"
    MEAN_SEA_LEVEL = "mean sea level"
    MEAN_TIDE_LEVEL = "mean tide level"
    ROTARY_BUSHING = "rotary bushing"
    ROTARY_TABLE = "rotary table"
    SEAFLOOR = "seafloor"
    WELLHEAD = "wellhead"
    WELL_SURFACE_LOCATION = "well surface location"
