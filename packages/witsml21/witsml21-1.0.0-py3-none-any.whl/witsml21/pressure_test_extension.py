from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_event_extension import AbstractEventExtension
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.volume_measure import VolumeMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PressureTestExtension(AbstractEventExtension):
    """
    Information on pressure test event.

    :ivar dia_orifice_size: Orifice Size
    :ivar dtime_next_test_date: Next Test Date
    :ivar flowrate_rate_bled: Rate Bled
    :ivar identifier_job: String Being Tested
    :ivar is_success: True if successful
    :ivar max_pressure_duration: Maximum pressure held during test
    :ivar circulating_position: Circulating position
    :ivar fluid_bled_type: Fluid bled type
    :ivar orientation_method: Description of orientaton method
    :ivar test_fluid_type: Test fluid type
    :ivar test_sub_type: Test sub type
    :ivar test_type: Test type
    :ivar annulus_pressure: Annulus pressure
    :ivar well_pressure_used: Well pressure used
    :ivar str10_reference: Reference #
    :ivar uid_assembly: Well (Assembly)
    :ivar volume_bled: Volume Bled
    :ivar volume_lost: Volume Lost
    :ivar volume_pumped: Volume Pumped
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    """
    dia_orifice_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaOrificeSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dtime_next_test_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimeNextTestDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    flowrate_rate_bled: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateRateBled",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    identifier_job: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentifierJob",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    is_success: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSuccess",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_pressure_duration: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "MaxPressureDuration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    circulating_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "CirculatingPosition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    fluid_bled_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FluidBledType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    orientation_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrientationMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    test_fluid_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestFluidType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    test_sub_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestSubType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    test_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    annulus_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AnnulusPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    well_pressure_used: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellPressureUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    str10_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Str10Reference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    uid_assembly: Optional[str] = field(
        default=None,
        metadata={
            "name": "UidAssembly",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    volume_bled: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeBled",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    volume_lost: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeLost",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    volume_pumped: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumePumped",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
