from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.absorbed_dose_uom import AbsorbedDoseUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbsorbedDoseMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AbsorbedDoseUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
