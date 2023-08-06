from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class TrajStationStatus(Enum):
    """
    Specifies the status of a trajectory station.

    :cvar OPEN: Has not been validated; does not influence position
        computation for stations below it.
    :cvar REJECTED: The quality is not ok; does not influence position
        computation for stations below it.
    :cvar POSITION: Validated and in-use.
    """
    OPEN = "open"
    REJECTED = "rejected"
    POSITION = "position"
