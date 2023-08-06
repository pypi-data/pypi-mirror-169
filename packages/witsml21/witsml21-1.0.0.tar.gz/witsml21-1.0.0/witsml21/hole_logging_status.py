from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class HoleLoggingStatus(Enum):
    """
    The status of the hole during logging.

    :cvar OPEN_HOLE: The hole has not been cased or cemented.
    :cvar CASED_HOLE: The hole has been cased but not cemented.
    :cvar CEMENTED_HOLE: The hole has been cased and cemented.
    """
    OPEN_HOLE = "open hole"
    CASED_HOLE = "cased hole"
    CEMENTED_HOLE = "cemented hole"
