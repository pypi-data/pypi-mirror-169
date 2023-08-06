from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.data_transfer_speed_uom import DataTransferSpeedUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DataTransferSpeedMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[DataTransferSpeedUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
