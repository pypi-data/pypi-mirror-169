from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class LicensePeriod:
    """
    This class is used to represent a period of time when a particular license
    was valid.

    :ivar num_license: License number.
    :ivar termination_date_time: The date and time when the license
        ceased to be effective.
    :ivar effective_date_time: The date and time when the license became
        effective.
    """
    num_license: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumLicense",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    termination_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminationDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    effective_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
