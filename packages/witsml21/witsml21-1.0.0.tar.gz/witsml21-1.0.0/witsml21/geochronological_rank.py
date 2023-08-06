from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class GeochronologicalRank(Enum):
    """
    Qualifier for the geological time denoted by the GeochronologicalUnit: eon,
    era, epoch, etc.
    """
    EON = "eon"
    ERA = "era"
    PERIOD = "period"
    EPOCH = "epoch"
    AGE = "age"
    CHRON = "chron"
