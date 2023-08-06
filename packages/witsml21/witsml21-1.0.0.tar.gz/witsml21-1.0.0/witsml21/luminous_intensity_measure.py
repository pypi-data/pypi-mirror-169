from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.luminous_intensity_uom import LuminousIntensityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LuminousIntensityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LuminousIntensityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
