from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class OperatingEnvironment(Enum):
    """
    The general location of a well or wellbore.

    :cvar ONSHORE: On land.
    :cvar MIDSHORE: Transitional marine environment.
    :cvar OFFSHORE: At sea with some distance from the shore.
    """
    ONSHORE = "onshore"
    MIDSHORE = "midshore"
    OFFSHORE = "offshore"
