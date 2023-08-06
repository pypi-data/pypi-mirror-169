from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class OperatingCondition(Enum):
    BENT_SUB = "bent sub"
    CABLE_CONVEYED = "cable conveyed"
    CASING = "casing"
    CASING_COLLAR_LOCATOR = "casing collar locator"
    CENTROLLERS = "centrollers"
    DRILL_PIPE = "drill pipe"
    DROPPED = "dropped"
    FAST_LOGGING_SPEED = "fast logging speed"
    FLOATING = "floating"
    LARGE_INSIDE_DIAMETER = "large inside diameter"
    SINGLE_SHOT = "single shot"
    SLOW_LOGGING_SPEED = "slow logging speed"
