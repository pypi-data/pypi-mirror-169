from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.plane_angle_operating_range import PlaneAngleOperatingRange

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AzimuthRange(PlaneAngleOperatingRange):
    """
    :ivar is_magnetic_north: True = magnetic north, False = True North
    """
    is_magnetic_north: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMagneticNorth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
