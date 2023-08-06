from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.pressure_measure import PressureMeasure
from witsml21.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimShutInPressure:
    """
    A pressure measurement taken at a certain time after the well has been shut
    in.

    :ivar pressure: The shut-in pressure.
    :ivar time_after_shutin: The time span after shut in at which the
        pressure was measured.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        StimShutInPressure.
    """
    pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    time_after_shutin: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "TimeAfterShutin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
