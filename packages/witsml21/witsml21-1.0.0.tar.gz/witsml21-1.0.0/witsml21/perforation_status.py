from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PerforationStatus(Enum):
    """
    Specifies the set of values for the status of a perforation.
    """
    OPEN = "open"
    PROPOSED = "proposed"
    SQUEEZED = "squeezed"
