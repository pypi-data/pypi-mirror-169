from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PerforationToolType(Enum):
    """
    Species the values for the type of perforation tool used to create the
    perfs.
    """
    CASING_GUN = "casing gun"
    COILED_TUBING_JET_TOOL = "coiled tubing jet tool"
    DRILLED = "drilled"
    MANDREL = "mandrel"
    N_A = "n/a"
    SLOTS_MACHINE_CUT = "slots-machine cut"
    SLOTS_UNDERCUT = "slots-undercut"
    STRIP_GUN = "strip gun"
    TCP_GUN = "tcp gun"
    THROUGH_TUBING_GUN = "through tubing gun"
