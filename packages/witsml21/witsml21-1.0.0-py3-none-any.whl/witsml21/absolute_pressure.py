from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_pressure_value import AbstractPressureValue
from witsml21.pressure_measure_ext import PressureMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbsolutePressure(AbstractPressureValue):
    absolute_pressure: Optional[PressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "AbsolutePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
