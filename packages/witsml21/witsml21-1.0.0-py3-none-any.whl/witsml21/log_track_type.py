from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class LogTrackType(Enum):
    """
    Specifies the kinds of track.

    :cvar CURVES:
    :cvar DATA:
    :cvar DEPTH: The index used by the track is depth
    :cvar TRACES:
    :cvar OTHER: The index used by the track is something other than
        depth.
    """
    CURVES = "curves"
    DATA = "data"
    DEPTH = "depth"
    TRACES = "traces"
    OTHER = "other"
