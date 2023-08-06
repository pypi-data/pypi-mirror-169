from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class NozzleType(Enum):
    """
    Specifies the type of nozzle.
    """
    EXTENDED = "extended"
    NORMAL = "normal"
