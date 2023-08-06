from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StratigraphyKindQualifier(Enum):
    BASE = "base"
    FAULT = "fault"
    GAS_OIL_CONTACT = "gas-oil contact"
    GAS_WATER_CONTACT = "gas-water contact"
    OIL_WATER_CONTACT = "oil-water contact"
    SEAFLOOR = "seafloor"
    TOP = "top"
