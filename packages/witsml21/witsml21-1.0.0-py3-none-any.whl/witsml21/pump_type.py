from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PumpType(Enum):
    """
    Specifies the type of pump.

    :cvar CENTRIFUGAL: Centrifugal mud pump.
    :cvar DUPLEX: Duplex mud mump, two cylinders.
    :cvar TRIPLEX: Triplex mud pump, three cylinders.
    """
    CENTRIFUGAL = "centrifugal"
    DUPLEX = "duplex"
    TRIPLEX = "triplex"
