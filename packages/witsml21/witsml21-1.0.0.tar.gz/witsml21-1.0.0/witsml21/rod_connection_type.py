from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_connection_type import AbstractConnectionType
from witsml21.rod_connection_types import RodConnectionTypes

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RodConnectionType(AbstractConnectionType):
    """
    A type of rod connection, e.g., latched, threaded, welded, etc.

    :ivar rod_connection_type: Connection whose type is rod.
    """
    rod_connection_type: Optional[RodConnectionTypes] = field(
        default=None,
        metadata={
            "name": "RodConnectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
