from __future__ import annotations
from dataclasses import dataclass
from witsml21.abstract_interval import AbstractInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractPressureInterval(AbstractInterval):
    pass
