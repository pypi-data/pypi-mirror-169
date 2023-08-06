from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.force_length_per_length_uom import ForceLengthPerLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ForceLengthPerLengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ForceLengthPerLengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
