from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ProppantAgentKind(Enum):
    """
    Specifies the type of proppant agent: ceramic, resin, sand, etc.
    """
    CERAMIC = "ceramic"
    RESIN_COATED_CERAMIC = "resin coated ceramic"
    RESIN_COATED_SAND = "resin coated sand"
    SAND = "sand"
