from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.mass_per_volume_per_length_uom import MassPerVolumePerLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerVolumePerLengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MassPerVolumePerLengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
