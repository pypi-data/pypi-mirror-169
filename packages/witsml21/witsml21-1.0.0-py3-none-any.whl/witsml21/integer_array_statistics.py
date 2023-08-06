from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IntegerArrayStatistics:
    valid_value_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValidValueCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    minimum_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    maximum_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    values_median: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValuesMedian",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    values_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValuesMode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    mode_percentage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ModePercentage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
