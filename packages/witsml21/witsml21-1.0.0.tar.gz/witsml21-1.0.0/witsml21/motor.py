from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.bearing_type import BearingType
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.plane_angle_measure import PlaneAngleMeasure
from witsml21.sensor import Sensor
from witsml21.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Motor:
    """Tubular Motor Component Schema.

    Used to capture properties about a motor used in a tubular string.

    :ivar offset_tool: Tool offset from bottom.
    :ivar pres_loss_fact: Pressure loss factor.
    :ivar flowrate_mn: Minimum flow rate.
    :ivar flowrate_mx: Maximum flow rate.
    :ivar dia_rotor_nozzle: Diameter of rotor at nozzle.
    :ivar clearance_bear_box: Clearance inside bearing box.
    :ivar lobes_rotor: Number of rotor lobes.
    :ivar lobes_stator: Number of stator lobes.
    :ivar type_bearing: Type of bearing.
    :ivar temp_op_mx: Maximum operating temperature.
    :ivar rotor_catcher: Is rotor catcher present? Values are "true" (or
        "1") and "false" (or "0").
    :ivar dump_valve: Is dump valve present? Values are "true" (or "1")
        and "false" (or "0").
    :ivar dia_nozzle: Nozzle diameter.
    :ivar rotatable: Is motor rotatable? Values are "true" (or "1") and
        "false" (or "0").
    :ivar bend_settings_mn: Minimum bend angle setting.
    :ivar bend_settings_mx: Maximum bend angle setting.
    :ivar sensor:
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    """
    offset_tool: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OffsetTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_loss_fact: Optional[float] = field(
        default=None,
        metadata={
            "name": "PresLossFact",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_mn: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_mx: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_rotor_nozzle: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaRotorNozzle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    clearance_bear_box: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ClearanceBearBox",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lobes_rotor: Optional[int] = field(
        default=None,
        metadata={
            "name": "LobesRotor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lobes_stator: Optional[int] = field(
        default=None,
        metadata={
            "name": "LobesStator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_bearing: Optional[BearingType] = field(
        default=None,
        metadata={
            "name": "TypeBearing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_op_mx: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempOpMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rotor_catcher: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RotorCatcher",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dump_valve: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DumpValve",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_nozzle: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaNozzle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rotatable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rotatable",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bend_settings_mn: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "BendSettingsMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bend_settings_mx: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "BendSettingsMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sensor: List[Sensor] = field(
        default_factory=list,
        metadata={
            "name": "Sensor",
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
