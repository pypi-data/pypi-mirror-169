from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellborePointOfInterest(Enum):
    BOTTOMHOLE_LOCATION = "bottomhole location"
    FIRST_PERFORATION = "first perforation"
    KICKOFF_POINT = "kickoff point"
    LANDING_POINT = "landing point"
    LAST_PERFORATION = "last perforation"
