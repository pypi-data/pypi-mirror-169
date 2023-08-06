from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class RiskCategory(Enum):
    """
    Specifies the category of risk.

    :cvar HYDRAULICS:
    :cvar MECHANICAL:
    :cvar TIME_RELATED: Specifies the category of risk.
    :cvar WELLBORE_STABILITY:
    :cvar DIRECTIONAL_DRILLING:
    :cvar BIT:
    :cvar EQUIPMENT_FAILURE:
    :cvar COMPLETION:
    :cvar CASING:
    :cvar OTHER:
    :cvar HSE: health, safety and environmental
    """
    HYDRAULICS = "hydraulics"
    MECHANICAL = "mechanical"
    TIME_RELATED = "time related"
    WELLBORE_STABILITY = "wellbore stability"
    DIRECTIONAL_DRILLING = "directional drilling"
    BIT = "bit"
    EQUIPMENT_FAILURE = "equipment failure"
    COMPLETION = "completion"
    CASING = "casing"
    OTHER = "other"
    HSE = "HSE"
