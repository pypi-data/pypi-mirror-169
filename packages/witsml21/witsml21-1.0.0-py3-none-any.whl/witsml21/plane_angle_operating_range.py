from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.abstract_operating_range import AbstractOperatingRange
from witsml21.plane_angle_uom import PlaneAngleUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PlaneAngleOperatingRange(AbstractOperatingRange):
    uom: Optional[Union[PlaneAngleUom, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
