from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.dynamic_viscosity_uom import DynamicViscosityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DynamicViscosityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[DynamicViscosityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
