from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TimeOrIntervalSeries:
    use_interval: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    time_series: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
