from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.pressure_per_flowrate_uom import PressurePerFlowrateUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressurePerFlowrateMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[PressurePerFlowrateUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".*:.*",
        }
    )
