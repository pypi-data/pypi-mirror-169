from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class CementJobType(Enum):
    """
    Specifies type of cement job.
    """
    PRIMARY = "primary"
    PLUG = "plug"
    SQUEEZE = "squeeze"
