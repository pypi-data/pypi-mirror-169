from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StimFlowPathType(Enum):
    """
    Specifies the type of flow paths used in a stimulation job.

    :cvar ANNULUS: Fluid is conducted through the annulus.
    :cvar CASING: Fluid is conducted through the casing (no tubing
        present).
    :cvar DRILL_PIPE: Fluid is conducted through the drill pipe.
    :cvar OPEN_HOLE: Fluid is conducted through the open hole.
    :cvar TUBING: Fluid is conducted through tubing.
    :cvar TUBING_AND_ANNULUS: Fluid is conducted through tubing and the
        annulus.
    """
    ANNULUS = "annulus"
    CASING = "casing"
    DRILL_PIPE = "drill pipe"
    OPEN_HOLE = "open hole"
    TUBING = "tubing"
    TUBING_AND_ANNULUS = "tubing and annulus"
