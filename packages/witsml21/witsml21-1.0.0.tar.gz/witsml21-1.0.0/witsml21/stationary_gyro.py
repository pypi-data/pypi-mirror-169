from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.gyro_axis_combination import GyroAxisCombination
from witsml21.plane_angle_operating_range import PlaneAngleOperatingRange

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StationaryGyro:
    axis_combination: Optional[GyroAxisCombination] = field(
        default=None,
        metadata={
            "name": "AxisCombination",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    range: Optional[PlaneAngleOperatingRange] = field(
        default=None,
        metadata={
            "name": "Range",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
