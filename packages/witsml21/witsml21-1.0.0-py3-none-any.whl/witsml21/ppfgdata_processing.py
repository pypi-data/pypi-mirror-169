from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PpfgdataProcessing(Enum):
    """
    The type and level of data processing that has been applied to PPFG data.
    """
    CALIBRATED = "calibrated"
    CORRECTED = "corrected"
    FILTERED = "filtered"
    INTERPOLATED = "interpolated"
    INTERPRETED = "interpreted"
    NORMALIZED = "normalized"
    SMOOTHED = "smoothed"
    TRANSFORMED = "transformed"
