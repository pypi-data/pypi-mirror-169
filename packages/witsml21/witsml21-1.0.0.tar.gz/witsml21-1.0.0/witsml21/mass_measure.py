from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.mass_uom import MassUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MassUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
