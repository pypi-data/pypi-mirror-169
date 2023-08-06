from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PassDetail:
    """
    Details about an individual pass when using PassIndexedDepth.

    :ivar pass_value: The pass number.
    :ivar description: Description of pass such as Calibration Pass,
        Main Pass, Repeated Pass.
    """
    pass_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
