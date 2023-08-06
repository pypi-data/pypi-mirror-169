from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_pressure_interval import AbstractPressureInterval
from witsml21.gauge_pressure import GaugePressure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GaugePressureInterval(AbstractPressureInterval):
    min_pressure: Optional[GaugePressure] = field(
        default=None,
        metadata={
            "name": "MinPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    max_pressure: Optional[GaugePressure] = field(
        default=None,
        metadata={
            "name": "MaxPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
