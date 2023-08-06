from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.electric_charge_per_area_uom import ElectricChargePerAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectricChargePerAreaMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ElectricChargePerAreaUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
