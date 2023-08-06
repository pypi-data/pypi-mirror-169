from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_pressure_value import AbstractPressureValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressureValue:
    abstract_pressure_value: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "AbstractPressureValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
