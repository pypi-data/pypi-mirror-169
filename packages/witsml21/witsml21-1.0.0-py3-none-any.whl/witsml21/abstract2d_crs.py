from __future__ import annotations
from dataclasses import dataclass
from witsml21.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Abstract2DCrs(AbstractObject):
    class Meta:
        name = "Abstract2dCrs"
