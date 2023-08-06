from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellInterest(Enum):
    """
    Reasons for interest in the well or information about the well.
    """
    OPERATED = "operated"
    NON_OPERATED_JOINT_VENTURE = "non-operated joint venture"
    COMPETITOR = "competitor"
