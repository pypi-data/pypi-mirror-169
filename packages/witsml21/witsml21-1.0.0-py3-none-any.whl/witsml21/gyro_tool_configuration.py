from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.accelerometer_axis_combination import AccelerometerAxisCombination
from witsml21.continuous_gyro import ContinuousGyro
from witsml21.stationary_gyro import StationaryGyro
from witsml21.xy_accelerometer import XyAccelerometer

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class GyroToolConfiguration:
    """
    SPE90408 Table 11 &amp; Appendix D.

    :ivar accelerometer_axis_combination: BR VS GyroMode
    :ivar external_reference:
    :ivar continuous_gyro:
    :ivar xy_accelerometer:
    :ivar stationary_gyro:
    """
    accelerometer_axis_combination: Optional[AccelerometerAxisCombination] = field(
        default=None,
        metadata={
            "name": "AccelerometerAxisCombination",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    external_reference: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    continuous_gyro: List[ContinuousGyro] = field(
        default_factory=list,
        metadata={
            "name": "ContinuousGyro",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    xy_accelerometer: Optional[XyAccelerometer] = field(
        default=None,
        metadata={
            "name": "XyAccelerometer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stationary_gyro: List[StationaryGyro] = field(
        default_factory=list,
        metadata={
            "name": "StationaryGyro",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
