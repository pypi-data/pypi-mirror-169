from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.gyro_axis_combination import GyroAxisCombination
from witsml21.length_measure_ext import LengthMeasureExt
from witsml21.length_per_time_measure_ext import LengthPerTimeMeasureExt
from witsml21.plane_angle_measure_ext import PlaneAngleMeasureExt
from witsml21.plane_angle_operating_range import PlaneAngleOperatingRange

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ContinuousGyro:
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
    gyro_reinitialization_distance: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "GyroReinitializationDistance",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    noise_reduction_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "NoiseReductionFactor",
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
    speed: Optional[LengthPerTimeMeasureExt] = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    initialization: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "Initialization",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
