from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BhaStatus(Enum):
    """
    Stage of the BHA Run (plan, progress, final)

    :cvar FINAL: Bha above rotary and the BhaRun DTimStop is populated
        with a value (e.g. the run is completed)
    :cvar PROGRESS: Active. The Bha is in the hole.
    :cvar PLAN: In planning stage.
    """
    FINAL = "final"
    PROGRESS = "progress"
    PLAN = "plan"
