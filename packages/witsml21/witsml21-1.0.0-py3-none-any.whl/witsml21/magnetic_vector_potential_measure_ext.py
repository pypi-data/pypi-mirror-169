from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.magnetic_vector_potential_uom import MagneticVectorPotentialUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticVectorPotentialMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MagneticVectorPotentialUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
