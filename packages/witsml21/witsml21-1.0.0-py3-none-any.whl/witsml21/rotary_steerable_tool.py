from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_rotary_steerable_tool import AbstractRotarySteerableTool
from witsml21.angular_velocity_measure import AngularVelocityMeasure
from witsml21.deflection_method import DeflectionMethod
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.force_measure import ForceMeasure
from witsml21.length_measure import LengthMeasure
from witsml21.sensor import Sensor
from witsml21.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RotarySteerableTool:
    """Rotary Steerable Tool Component Schema.

    Captures size and performance information about the rotary steerable
    tool used in the tubular string.

    :ivar deflection_method: Method used to direct the deviation of the
        trajectory: point bit or push bit.
    :ivar hole_size_mn: Minimum size of the hole in which the tool can
        operate.
    :ivar hole_size_mx: Maximum size of the hole in which the tool can
        operate.
    :ivar wob_mx: Maximum weight on the bit.
    :ivar operating_speed: Suggested operating speed.
    :ivar speed_mx: Maximum rotation speed.
    :ivar flow_rate_mn: Minimum flow rate for tool operation.
    :ivar flow_rate_mx: Maximum flow rate for tool operation.
    :ivar down_link_flow_rate_mn: Minimum flow rate for programming the
        tool.
    :ivar down_link_flow_rate_mx: Maximum flow rate for programming the
        tool.
    :ivar press_loss_fact: Pressure drop across the tool.
    :ivar pad_count: The number of contact pads.
    :ivar pad_len: Length of the contact pad.
    :ivar pad_width: Width of the contact pad.
    :ivar pad_offset: Offset from the bottom of the pad to the bottom
        connector.
    :ivar open_pad_od: Outside diameter of the tool when the pads are
        activated.
    :ivar close_pad_od: Outside diameter of the tool when the pads are
        closed.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar tool:
    :ivar sensor:
    """
    deflection_method: Optional[DeflectionMethod] = field(
        default=None,
        metadata={
            "name": "DeflectionMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    hole_size_mn: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HoleSizeMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hole_size_mx: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HoleSizeMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wob_mx: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "WobMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    operating_speed: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "OperatingSpeed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    speed_mx: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "SpeedMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flow_rate_mn: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowRateMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flow_rate_mx: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowRateMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    down_link_flow_rate_mn: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "DownLinkFlowRateMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    down_link_flow_rate_mx: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "DownLinkFlowRateMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    press_loss_fact: Optional[float] = field(
        default=None,
        metadata={
            "name": "PressLossFact",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pad_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PadCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pad_len: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PadLen",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pad_width: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PadWidth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pad_offset: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PadOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    open_pad_od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OpenPadOd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    close_pad_od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ClosePadOd",
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
    tool: Optional[AbstractRotarySteerableTool] = field(
        default=None,
        metadata={
            "name": "Tool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
