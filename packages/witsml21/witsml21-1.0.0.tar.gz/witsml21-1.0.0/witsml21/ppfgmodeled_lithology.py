from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PpfgmodeledLithology(Enum):
    """
    Specifies the type of lithology modeled in PPFG data.
    """
    CARBONATE = "carbonate"
    COMPOSITE = "composite"
    IGNEOUS = "igneous"
    SALT = "salt"
    SAND = "sand"
    SHALE = "shale"
