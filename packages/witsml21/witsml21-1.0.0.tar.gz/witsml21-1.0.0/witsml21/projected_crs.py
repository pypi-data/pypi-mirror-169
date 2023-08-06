from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.abstract_projected_crs import AbstractProjectedCrs
from witsml21.axis_order2d import AxisOrder2D
from witsml21.cartesian2d_crs import Cartesian2DCrs
from witsml21.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedCrs(Cartesian2DCrs):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    axis_order: Optional[AxisOrder2D] = field(
        default=None,
        metadata={
            "name": "AxisOrder",
            "type": "Element",
            "required": True,
        }
    )
    abstract_projected_crs: Optional[AbstractProjectedCrs] = field(
        default=None,
        metadata={
            "name": "AbstractProjectedCrs",
            "type": "Element",
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".*:.*",
        }
    )
