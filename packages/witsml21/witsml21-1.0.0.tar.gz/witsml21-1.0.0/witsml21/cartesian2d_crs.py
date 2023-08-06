from __future__ import annotations
from dataclasses import dataclass
from witsml21.abstract2d_crs import Abstract2DCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Cartesian2DCrs(Abstract2DCrs):
    class Meta:
        name = "Cartesian2dCrs"
