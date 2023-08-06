from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.length_measure_ext import LengthMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractElevation:
    elevation: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "Elevation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
