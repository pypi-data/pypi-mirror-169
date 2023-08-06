from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.pressure_per_flowrate_uom import PressurePerFlowrateUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressurePerFlowrateMeasure:
    """
    PressurePerFlowrateSquared, P/Q^2 is the unit for turbulent flow pressure
    drop in the layer inflow relationship.

    :ivar value:
    :ivar uom: One of uoms from PressurePerFlowrateUom list
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PressurePerFlowrateUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
