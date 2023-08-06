from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PumpOpType(Enum):
    """
    Specifies type of well operation being conducted while this pump was in
    use.
    """
    DRILLING = "drilling"
    REAMING = "reaming"
    CIRCULATING = "circulating"
    SLOW_PUMP = "slow pump"
