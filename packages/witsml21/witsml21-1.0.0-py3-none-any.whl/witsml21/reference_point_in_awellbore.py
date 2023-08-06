from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_measure_ext import LengthMeasureExt
from witsml21.recursive_reference_point import RecursiveReferencePoint

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReferencePointInAwellbore(RecursiveReferencePoint):
    """A reference point which is defined in the context of a wellbore by means
    of a MD.

    If TVD is needed, it must be given through the inherited vertical
    Coordinate.

    :ivar md: The measured depth (depth along the wellbore) from the
        reference point to its BaseReferencePoint.
    :ivar trajectory: An optional Trajectory used in calculation of the
        VerticalCoordinate if present, especially if the
        VerticalCoordinate is in TVD.
    :ivar wellbore: The wellbore holding the reference point.
    """
    class Meta:
        name = "ReferencePointInAWellbore"
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    md: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "required": True,
        }
    )
    trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
