from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.amount_of_substance_per_time_per_area_uom import AmountOfSubstancePerTimePerAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AmountOfSubstancePerTimePerAreaMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AmountOfSubstancePerTimePerAreaUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
