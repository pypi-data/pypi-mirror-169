from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.pressure_measure import PressureMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimPressureFlowRate:
    """
    In an injection step test, the injection rate at a particular pressure.

    :ivar pressure: The pressure of the step test.
    :ivar bottomhole_rate: The flow of the fluid at the bottomhole.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        StimPressureFlowRate.
    """
    pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bottomhole_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "BottomholeRate",
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
