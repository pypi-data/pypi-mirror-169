from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.magnetic_dipole_moment_uom import MagneticDipoleMomentUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticDipoleMomentMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MagneticDipoleMomentUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
