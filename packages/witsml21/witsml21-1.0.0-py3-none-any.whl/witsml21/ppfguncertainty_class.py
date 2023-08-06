from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PpfguncertaintyType(Enum):
    """
    Specifies class of uncertainty for PPFG data.
    """
    HIGH = "high"
    LOW = "low"
    MAXIMUM = "maximum"
    MEAN = "mean"
    MID = "mid"
    MINIMUM = "minimum"
    MOST_LIKELY = "most likely"
    P10 = "p10"
    P50 = "p50"
    P90 = "p90"
