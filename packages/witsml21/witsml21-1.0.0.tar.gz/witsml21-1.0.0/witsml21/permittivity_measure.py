from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.permittivity_uom import PermittivityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PermittivityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PermittivityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
