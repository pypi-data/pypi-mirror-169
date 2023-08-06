from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.time_per_mass_uom import TimePerMassUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TimePerMassMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[TimePerMassUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
