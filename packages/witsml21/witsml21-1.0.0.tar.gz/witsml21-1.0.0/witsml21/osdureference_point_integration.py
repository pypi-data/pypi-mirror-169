from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class OsdureferencePointIntegration:
    """
    OSDU-specific details about reference point.

    :ivar effective_date_time: The date and time when the reference
        point became effective.
    :ivar termination_date_time: The data and time when the reference
        point ceased to be effective.
    """
    class Meta:
        name = "OSDUReferencePointIntegration"

    effective_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    termination_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminationDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
