from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class OsdutubularAssemblyStatus:
    """
    OSDU Tubular Assembly Status information.

    :ivar date: Date the status has been established.
    :ivar description: Used to describe the reason of Activity - such as
        cut/pull, pulling.
    :ivar status_type: Status type.
    """
    class Meta:
        name = "OSDUTubularAssemblyStatus"

    date: Optional[str] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 256,
        }
    )
    status_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
