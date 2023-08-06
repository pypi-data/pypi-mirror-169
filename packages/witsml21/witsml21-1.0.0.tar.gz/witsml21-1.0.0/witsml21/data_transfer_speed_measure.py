from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_transfer_speed_uom import DataTransferSpeedUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DataTransferSpeedMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[DataTransferSpeedUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
