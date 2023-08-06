from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_object import AbstractObject
from witsml21.azimuth_formula import AzimuthFormula
from witsml21.continuous_azimuth_formula import ContinuousAzimuthFormula
from witsml21.error_kind import ErrorKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WeightingFunction(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "max_length": 2000,
        }
    )
    kind: Optional[ErrorKind] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
        }
    )
    source: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Source",
            "type": "Element",
            "max_length": 64,
        }
    )
    depth_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepthFormula",
            "type": "Element",
            "required": True,
            "max_length": 2000,
        }
    )
    inclination_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "InclinationFormula",
            "type": "Element",
            "required": True,
            "max_length": 2000,
        }
    )
    singularity_north_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "SingularityNorthFormula",
            "type": "Element",
            "max_length": 2000,
        }
    )
    singularity_east_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "SingularityEastFormula",
            "type": "Element",
            "max_length": 2000,
        }
    )
    singularity_vertical_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "SingularityVerticalFormula",
            "type": "Element",
            "max_length": 2000,
        }
    )
    azimuth_formula: Optional[AzimuthFormula] = field(
        default=None,
        metadata={
            "name": "AzimuthFormula",
            "type": "Element",
            "required": True,
        }
    )
    continuous_azimuth_formula: List[ContinuousAzimuthFormula] = field(
        default_factory=list,
        metadata={
            "name": "ContinuousAzimuthFormula",
            "type": "Element",
            "max_occurs": 3,
        }
    )
