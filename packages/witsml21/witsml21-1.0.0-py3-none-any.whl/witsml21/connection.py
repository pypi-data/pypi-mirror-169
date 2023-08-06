from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.area_measure import AreaMeasure
from witsml21.connection_position import ConnectionPosition
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.moment_of_force_measure import MomentOfForceMeasure
from witsml21.pressure_measure import PressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Connection:
    """Tubular Connection Component Schema.

    Describes dimensions and properties of a connection between
    tubulars.

    :ivar id: Inside diameter of the connection.
    :ivar od: Outside diameter of the body of the item.
    :ivar len: Length of the item.
    :ivar type_thread: Thread type from API RP7G, 5CT.
    :ivar size_thread: Thread size.
    :ivar tens_yield: Yield stress of steel: worn stress.
    :ivar tq_yield: Torque at which yield occurs.
    :ivar position: Where connected.
    :ivar critical_cross_section: For bending stiffness ratio.
    :ivar pres_leak: Leak pressure rating.
    :ivar tq_makeup: Make-up torque.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Connection.
    """
    id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Len",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_thread: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeThread",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    size_thread: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SizeThread",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tens_yield: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "TensYield",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_yield: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqYield",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    position: Optional[ConnectionPosition] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    critical_cross_section: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "CriticalCrossSection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_leak: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresLeak",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_makeup: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqMakeup",
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
