from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.address_qualifier import AddressQualifier

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class EmailQualifierStruct:
    """
    An email address with an attribute, used to "qualify" an email as personal,
    work, or permanent.

    :ivar value:
    :ivar qualifier: Enum attribute, used to "qualify" an email as
        personal, work, or permanent.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        }
    )
    qualifier: Optional[AddressQualifier] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
