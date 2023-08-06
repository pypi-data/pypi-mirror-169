from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractGeographic2DCrs:
    class Meta:
        name = "AbstractGeographic2dCrs"
