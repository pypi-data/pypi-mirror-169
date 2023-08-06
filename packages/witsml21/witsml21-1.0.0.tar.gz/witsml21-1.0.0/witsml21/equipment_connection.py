from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_connection_type import AbstractConnectionType
from witsml21.component_reference import ComponentReference
from witsml21.connection import Connection
from witsml21.connection_form_type import ConnectionFormType
from witsml21.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class EquipmentConnection(Connection):
    """
    Information detailing the connection between two components.

    :ivar equipment: Reference to the string equipment.
    :ivar radial_offset: Measurement of radial offset.
    :ivar connection_form: The form of connection: box or pin.
    :ivar connection_upset: Connection upset.
    :ivar connection_type:
    """
    equipment: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    radial_offset: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "RadialOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    connection_form: Optional[ConnectionFormType] = field(
        default=None,
        metadata={
            "name": "ConnectionForm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    connection_upset: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionUpset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    connection_type: Optional[AbstractConnectionType] = field(
        default=None,
        metadata={
            "name": "ConnectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
