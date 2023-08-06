from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.magnetic_field_strength_uom import MagneticFieldStrengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticFieldStrengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MagneticFieldStrengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
