from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.volume_per_rotation_uom import VolumePerRotationUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerRotationMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumePerRotationUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
