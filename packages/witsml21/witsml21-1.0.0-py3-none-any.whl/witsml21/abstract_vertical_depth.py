from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_measure_ext import LengthMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractVerticalDepth:
    """A vertical (gravity-based) depth coordinate within the context of a
    well.

    Positive moving downward from the reference datum. All coordinates
    with the same datum (and same UOM) can be considered to be in the
    same coordinate reference system (CRS) and are thus directly
    comparable.
    """
    vertical_depth: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "VerticalDepth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
