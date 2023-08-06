from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.plane_angle_measure_ext import PlaneAngleMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class XyAccelerometer:
    cant_angle: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "CantAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    switching: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Switching",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
