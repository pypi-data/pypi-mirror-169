from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PressureGradientParameterKind(Enum):
    """
    Specifies values for mud log parameters that are measured in units of
    pressure gradient.
    """
    DIRECT_PORE_PRESSURE_GRADIENT_MEASUREMENT = "direct pore pressure gradient measurement"
    FRACTURE_PRESSURE_GRADIENT_ESTIMATE = "fracture pressure gradient estimate"
    KICK_PRESSURE_GRADIENT = "kick pressure gradient"
    LOST_RETURNS = "lost returns"
    OVERBURDEN_GRADIENT = "overburden gradient"
    PORE_PRESSURE_GRADIENT_ESTIMATE = "pore pressure gradient estimate"
