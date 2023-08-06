from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.cation_exchange_capacity_uom import CationExchangeCapacityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class CationExchangeCapacityMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[CationExchangeCapacityUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
