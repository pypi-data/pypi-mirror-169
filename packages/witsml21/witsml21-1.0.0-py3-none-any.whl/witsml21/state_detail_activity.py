from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StateDetailActivity(Enum):
    """
    Specifies the state of a drilling activity (DrillActivity).

    :cvar INJURY: Personnel injury in connection with drilling and/or
        drilling related operations.
    :cvar OPERATION_FAILED: Operation failed to achieve objective.
    :cvar KICK: Formation fluid invading the wellbore.
    :cvar CIRCULATION_LOSS: Circulation lost to the formation.
    :cvar MUD_LOSS: Circulation impossible due to plugging or failure of
        equipment.
    :cvar STUCK_EQUIPMENT: Equipment got stuck in the hole.
    :cvar EQUIPMENT_FAILURE: Equipment failure occurred.
    :cvar EQUIPMENT_HANG: Operations had to be aborted due to an
        equipment issue
    :cvar SUCCESS: Operation achieved  the objective.
    """
    INJURY = "injury"
    OPERATION_FAILED = "operation failed"
    KICK = "kick"
    CIRCULATION_LOSS = "circulation loss"
    MUD_LOSS = "mud loss"
    STUCK_EQUIPMENT = "stuck equipment"
    EQUIPMENT_FAILURE = "equipment failure"
    EQUIPMENT_HANG = "equipment hang"
    SUCCESS = "success"
