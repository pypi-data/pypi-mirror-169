from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.permeability_rock_uom import PermeabilityRockUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PermeabilityRockMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PermeabilityRockUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
