from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.component_reference import ComponentReference
from witsml21.length_measure import LengthMeasure
from witsml21.volume_measure import VolumeMeasure
from witsml21.wellbore_fluid_location import WellboreFluidLocation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class FluidLocation:
    """
    Location of fluid in the wellbore.

    :ivar fluid: Reference to fluid used in the CementJob.
    :ivar mdfluid_base: Measured depth of the base of the cement.
    :ivar mdfluid_top: Measured depth at the top of the interval.
    :ivar volume: Volume of fluid at this location.
    :ivar location_type:
    :ivar uid: Unique identifier for this instance of FluidLocation.
    """
    fluid: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "Fluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    mdfluid_base: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MDFluidBase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    mdfluid_top: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MDFluidTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    location_type: Optional[WellboreFluidLocation] = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
