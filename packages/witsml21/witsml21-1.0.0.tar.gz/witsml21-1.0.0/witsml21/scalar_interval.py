from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_interval import AbstractInterval
from witsml21.generic_measure import GenericMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ScalarInterval(AbstractInterval):
    min_value: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "MinValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    max_value: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "MaxValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
