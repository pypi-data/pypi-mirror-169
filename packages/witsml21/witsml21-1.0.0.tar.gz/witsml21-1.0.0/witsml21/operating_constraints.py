from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.azimuth_range import AzimuthRange
from witsml21.custom_operating_range import CustomOperatingRange
from witsml21.generic_measure import GenericMeasure
from witsml21.md_interval import MdInterval
from witsml21.plane_angle_measure_ext import PlaneAngleMeasureExt
from witsml21.plane_angle_operating_range import PlaneAngleOperatingRange
from witsml21.pressure_measure_ext import PressureMeasureExt
from witsml21.thermodynamic_temperature_measure_ext import ThermodynamicTemperatureMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class OperatingConstraints:
    """
    :ivar custom_limits:
    :ivar horizontal_east_west_max_value: Absolute value of the maximum
        value allowed for the product sin(Inclination) * sin(Azimuth).
    :ivar md_range:
    :ivar tvd_range:
    :ivar pressure_limit:
    :ivar thermodynamic_temperature_limit:
    :ivar custom_range: Can be segmented
    :ivar latitude_range: Can be segmented
    :ivar inclination_range: Can be segmented
    :ivar azimuth_range: Can be segmented
    """
    custom_limits: List[GenericMeasure] = field(
        default_factory=list,
        metadata={
            "name": "CustomLimits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    horizontal_east_west_max_value: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "HorizontalEastWestMaxValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_range: List[MdInterval] = field(
        default_factory=list,
        metadata={
            "name": "MdRange",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_range: List[AbstractTvdInterval] = field(
        default_factory=list,
        metadata={
            "name": "TvdRange",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pressure_limit: Optional[PressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "PressureLimit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    thermodynamic_temperature_limit: Optional[ThermodynamicTemperatureMeasureExt] = field(
        default=None,
        metadata={
            "name": "ThermodynamicTemperatureLimit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    custom_range: List[CustomOperatingRange] = field(
        default_factory=list,
        metadata={
            "name": "CustomRange",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    latitude_range: List[PlaneAngleOperatingRange] = field(
        default_factory=list,
        metadata={
            "name": "LatitudeRange",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    inclination_range: List[PlaneAngleOperatingRange] = field(
        default_factory=list,
        metadata={
            "name": "InclinationRange",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    azimuth_range: List[AzimuthRange] = field(
        default_factory=list,
        metadata={
            "name": "AzimuthRange",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
