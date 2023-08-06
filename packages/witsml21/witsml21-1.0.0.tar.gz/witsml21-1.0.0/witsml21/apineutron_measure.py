from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.apineutron_uom import ApineutronUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ApineutronMeasure:
    class Meta:
        name = "APINeutronMeasure"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ApineutronUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
