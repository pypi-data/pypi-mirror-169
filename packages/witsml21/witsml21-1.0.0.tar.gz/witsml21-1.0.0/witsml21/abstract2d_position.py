from __future__ import annotations
from dataclasses import dataclass
from witsml21.abstract_position import AbstractPosition

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Abstract2DPosition(AbstractPosition):
    class Meta:
        name = "Abstract2dPosition"
