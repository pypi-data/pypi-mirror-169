from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PitType(Enum):
    """
    Specfies the type of pit.

    :cvar BULK:
    :cvar CHEMICAL:
    :cvar DRILLING:
    :cvar MIX:
    :cvar MUD_CLEANING:
    :cvar SAND_TRAP:
    :cvar SLUG: The pit in the active pit system located immediately
        downstream of the shale shakers, whose primary purpose is to
        allow the settling and disposal of the larger drilled cuttings
        not removed by the shale shakers. It is also called a settling
        tank".
    :cvar STORAGE:
    :cvar SURGE_TANK:
    :cvar TRIP_TANK:
    """
    BULK = "bulk"
    CHEMICAL = "chemical"
    DRILLING = "drilling"
    MIX = "mix"
    MUD_CLEANING = "mud cleaning"
    SAND_TRAP = "sand trap"
    SLUG = "slug"
    STORAGE = "storage"
    SURGE_TANK = "surge tank"
    TRIP_TANK = "trip tank"
