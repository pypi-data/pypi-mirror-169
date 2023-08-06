from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ConnectionPosition(Enum):
    """
    Specifies the position of a connection.

    :cvar BOTH: The connection is the same at both ends of the
        component.
    :cvar BOTTOM: This connection is only at the bottom of the
        component.
    :cvar TOP: This connection is only at the top of the component.
    """
    BOTH = "both"
    BOTTOM = "bottom"
    TOP = "top"
