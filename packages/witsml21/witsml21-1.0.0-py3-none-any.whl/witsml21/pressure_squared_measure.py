from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.pressure_squared_uom import PressureSquaredUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressureSquaredMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PressureSquaredUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
