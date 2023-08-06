from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class LogRectangleType(Enum):
    """
    Specifies the type of content from the original log defined by the
    rectangle.

    :cvar HEADER: Denotes rectangle bounds a header section
    :cvar ALTERNATE:
    """
    HEADER = "header"
    ALTERNATE = "alternate"
