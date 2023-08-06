from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.thermal_resistance_uom import ThermalResistanceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ThermalResistanceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ThermalResistanceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
