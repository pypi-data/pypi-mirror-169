from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class RiskType(Enum):
    """
    Specifies the type of risk.
    """
    RISK = "risk"
    EVENT = "event"
    NEAR_MISS = "near miss"
    BEST_PRACTICE = "best practice"
    LESSONS_LEARNED = "lessons learned"
    OTHER = "other"
