from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.mass_per_volume_uom_with_legacy import MassPerVolumeUomWithLegacy

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerVolumeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MassPerVolumeUomWithLegacy] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
