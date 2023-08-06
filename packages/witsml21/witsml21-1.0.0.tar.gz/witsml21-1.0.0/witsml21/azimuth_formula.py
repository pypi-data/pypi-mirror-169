from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.parameter import Parameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AzimuthFormula:
    formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "Formula",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 2000,
        }
    )
    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
