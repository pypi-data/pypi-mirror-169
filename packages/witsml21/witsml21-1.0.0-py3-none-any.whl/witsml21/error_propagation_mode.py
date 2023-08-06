from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ErrorPropagationMode(Enum):
    B = "B"
    G = "G"
    R = "R"
    S = "S"
    W = "W"
