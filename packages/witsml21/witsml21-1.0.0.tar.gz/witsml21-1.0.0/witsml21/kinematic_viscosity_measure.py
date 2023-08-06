from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.kinematic_viscosity_uom import KinematicViscosityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class KinematicViscosityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[KinematicViscosityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
