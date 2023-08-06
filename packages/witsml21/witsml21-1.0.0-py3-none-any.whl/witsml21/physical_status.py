from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PhysicalStatus(Enum):
    """
    Specifies the values for the physical status of an interval.
    """
    CLOSED = "closed"
    OPEN = "open"
    PROPOSED = "proposed"
