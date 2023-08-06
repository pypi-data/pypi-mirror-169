from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.force_per_force_uom import ForcePerForceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ForcePerForceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ForcePerForceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
