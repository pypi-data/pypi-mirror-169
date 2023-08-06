from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ShowRating(Enum):
    """
    Specifies the quality of the fluid showing at this interval.
    """
    NONE = "none"
    VERY_POOR = "very poor"
    POOR = "poor"
    FAIR = "fair"
    GOOD = "good"
    VERY_GOOD = "very good"
