from __future__ import annotations
from dataclasses import dataclass
from witsml21.abstract_value_array import AbstractValueArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractNumericArray(AbstractValueArray):
    pass
