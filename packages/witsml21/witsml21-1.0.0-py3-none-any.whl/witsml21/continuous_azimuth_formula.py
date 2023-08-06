from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.azimuth_formula import AzimuthFormula
from witsml21.gyro_axis_combination import GyroAxisCombination

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ContinuousAzimuthFormula(AzimuthFormula):
    gyro_axis: Optional[GyroAxisCombination] = field(
        default=None,
        metadata={
            "name": "GyroAxis",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
