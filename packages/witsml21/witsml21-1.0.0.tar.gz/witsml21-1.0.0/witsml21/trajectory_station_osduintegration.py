from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.length_measure import LengthMeasure
from witsml21.length_measure_ext import LengthMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TrajectoryStationOsduintegration:
    """
    Information about a TrajectoryStation that is relevant for OSDU integration
    but does not have a natural place in a TrajectoryStation object.

    :ivar easting: The easting value of the point in the directional
        survey. Local CRS must be defined.
    :ivar northing: The northing value of the point in the directional
        survey. Local CRS must be defined.
    :ivar radius_of_uncertainty: The radius of uncertainty distance of
        this trajectory station.
    """
    class Meta:
        name = "TrajectoryStationOSDUIntegration"

    easting: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "Easting",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    northing: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "Northing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    radius_of_uncertainty: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "RadiusOfUncertainty",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
