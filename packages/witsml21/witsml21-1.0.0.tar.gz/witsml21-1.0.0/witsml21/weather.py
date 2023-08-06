from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.length_per_time_measure import LengthPerTimeMeasure
from witsml21.plane_angle_measure import PlaneAngleMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml21.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Weather:
    """
    Operations Weather Component Schema.

    :ivar dtim: Date and time the information is related to.
    :ivar agency: Pointer to a BusinessAssociate representing the
        company that supplied the weather data.
    :ivar barometric_pressure: Atmospheric pressure.
    :ivar beaufort_scale_number: The Beaufort wind force scale is a
        system used to estimate and report wind speeds when no measuring
        apparatus is available. It was invented in the early 19th
        century by Admiral Sir Francis Beaufort of the British Navy as a
        way to interpret winds from conditions. Values range from 0
        (calm) to 12 (hurricane force).
    :ivar temp_surface_mn: Minimum temperature above ground. Temperature
        of the atmosphere.
    :ivar temp_surface_mx: Maximum temperature above ground.
    :ivar temp_wind_chill: A measure of the combined chilling effect of
        wind and low temperature on living things, also named chill
        factor, e.g., according to the US weather service table, an air
        temperature of 30 degF with a 10 mph corresponds to a windchill
        of 22 degF.
    :ivar tempsea: Sea temperature.
    :ivar visibility: Horizontal visibility.
    :ivar azi_wave: The direction from which the waves are coming,
        measured from true north.
    :ivar ht_wave: Average height of the waves.
    :ivar significant_wave: An average of the higher 1/3 of the wave
        heights passing during a  sample period (typically 20 to 30
        minutes).
    :ivar max_wave: The maximum wave height.
    :ivar period_wave: The elapsed time between the passing of two wave
        tops.
    :ivar azi_wind: The direction from which the wind is blowing,
        measured from true north.
    :ivar vel_wind: Wind speed.
    :ivar type_precip: Type of precipitation.
    :ivar amt_precip: Amount of precipitation.
    :ivar cover_cloud: Description of cloud cover.
    :ivar ceiling_cloud: Height of cloud cover.
    :ivar current_sea: The speed of the ocean current.
    :ivar azi_current_sea: Azimuth of current.
    :ivar comments: Comments and remarks.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Weather
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    agency: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Agency",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    barometric_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "BarometricPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    beaufort_scale_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BeaufortScaleNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+",
        }
    )
    temp_surface_mn: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempSurfaceMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_surface_mx: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempSurfaceMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_wind_chill: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempWindChill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tempsea: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "Tempsea",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    visibility: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Visibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    azi_wave: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AziWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ht_wave: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HtWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    significant_wave: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SignificantWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_wave: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaxWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    period_wave: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "PeriodWave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    azi_wind: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AziWind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vel_wind: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "VelWind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_precip: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypePrecip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    amt_precip: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "AmtPrecip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cover_cloud: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoverCloud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    ceiling_cloud: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "CeilingCloud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    current_sea: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "CurrentSea",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    azi_current_sea: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AziCurrentSea",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
