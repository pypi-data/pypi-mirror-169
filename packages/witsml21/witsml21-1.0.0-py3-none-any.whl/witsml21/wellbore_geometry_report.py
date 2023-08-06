from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.length_measure_ext import LengthMeasureExt
from witsml21.wellbore_geometry_section import WellboreGeometrySection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreGeometryReport:
    """
    Captures information for a report including wellbore geometry.

    :ivar wellbore_geometry_section:
    :ivar depth_water_mean: Water depth.
    :ivar gap_air: Air gap.
    """
    wellbore_geometry_section: List[WellboreGeometrySection] = field(
        default_factory=list,
        metadata={
            "name": "WellboreGeometrySection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    depth_water_mean: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "DepthWaterMean",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gap_air: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "GapAir",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
