from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_growing_object import AbstractMdGrowingObject
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_measure_ext import LengthMeasureExt
from witsml21.wellbore_geometry_section import WellboreGeometrySection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreGeometry(AbstractMdGrowingObject):
    """Used to capture information about the configuration of the permanently
    installed components in a wellbore.

    This object is uniquely identified within the context of one
    wellbore object.

    :ivar wellbore_geometry_section:
    :ivar wellbore:
    :ivar bha_run:
    :ivar depth_water_mean: Water depth.
    :ivar gap_air: Air gap.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    wellbore_geometry_section: List[WellboreGeometrySection] = field(
        default_factory=list,
        metadata={
            "name": "WellboreGeometrySection",
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
    bha_run: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "BhaRun",
            "type": "Element",
        }
    )
    depth_water_mean: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "DepthWaterMean",
            "type": "Element",
        }
    )
    gap_air: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "GapAir",
            "type": "Element",
        }
    )
