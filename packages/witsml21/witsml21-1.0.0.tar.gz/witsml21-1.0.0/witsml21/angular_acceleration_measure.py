from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.angular_acceleration_uom import AngularAccelerationUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AngularAccelerationMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AngularAccelerationUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
