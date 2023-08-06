from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_compound_position import AbstractCompoundPosition
from witsml21.projected_compound_crs import ProjectedCompoundCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedCompoundPosition(AbstractCompoundPosition):
    coordinate1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    coordinate2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    vertical_coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "VerticalCoordinate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    projected_compound_crs: Optional[ProjectedCompoundCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCompoundCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
