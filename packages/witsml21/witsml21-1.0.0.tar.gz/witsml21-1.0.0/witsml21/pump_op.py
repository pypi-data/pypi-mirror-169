from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.angular_velocity_measure import AngularVelocityMeasure
from witsml21.component_reference import ComponentReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.measured_depth import MeasuredDepth
from witsml21.power_per_power_measure import PowerPerPowerMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.pump_op_type import PumpOpType
from witsml21.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PumpOp:
    """
    Operations Pump Component Schema.

    :ivar dtim: Date and time the information is related to.
    :ivar pump: A pointer to the corresponding pump on the rig.
    :ivar type_operation: Type of pump operation.
    :ivar id_liner: Liner inside diameter.
    :ivar len_stroke: Stroke length.
    :ivar rate_stroke: Pump rate (strokes per minute).
    :ivar pressure: Pump pressure recorded.
    :ivar pc_efficiency: Pump efficiency.
    :ivar pump_output: Pump output (included for efficiency).
    :ivar md_bit: Along-hole measured depth of the measurement from the
        drill datum.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of PumpOp.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    pump: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "Pump",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    type_operation: Optional[PumpOpType] = field(
        default=None,
        metadata={
            "name": "TypeOperation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_liner: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdLiner",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_stroke: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenStroke",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rate_stroke: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "RateStroke",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    pc_efficiency: Optional[PowerPerPowerMeasure] = field(
        default=None,
        metadata={
            "name": "PcEfficiency",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pump_output: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "PumpOutput",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_bit: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdBit",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
