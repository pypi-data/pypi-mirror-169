from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LightExposureUom(Enum):
    """
    :cvar FOOTCANDLE_S: footcandle second
    :cvar LX_S: lux second
    """
    FOOTCANDLE_S = "footcandle.s"
    LX_S = "lx.s"
