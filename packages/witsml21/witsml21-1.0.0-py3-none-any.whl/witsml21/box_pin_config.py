from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BoxPinConfig(Enum):
    """
    Specifies values that represent the type of box and pin configuration.
    """
    BOTTOM_BOX_TOP_BOX = "bottom box top box"
    BOTTOM_BOX_TOP_PIN = "bottom box top pin"
    BOTTOM_PIN_TOP_PIN = "bottom pin top pin"
    BOTTOM_PIN_TOP_BOX = "bottom pin top box"
