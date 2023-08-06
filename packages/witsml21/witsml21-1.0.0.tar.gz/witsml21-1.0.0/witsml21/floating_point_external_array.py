from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_floating_point_array import AbstractFloatingPointArray
from witsml21.external_data_array import ExternalDataArray
from witsml21.floating_point_type import FloatingPointType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FloatingPointExternalArray(AbstractFloatingPointArray):
    """An array of double values provided explicitly by an HDF5 dataset.

    By convention, the null value is NaN.

    :ivar array_floating_point_type:
    :ivar count_per_value:
    :ivar values: Reference to an HDF5 array of doubles.
    """
    array_floating_point_type: Optional[FloatingPointType] = field(
        default=None,
        metadata={
            "name": "ArrayFloatingPointType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    count_per_value: int = field(
        default=1,
        metadata={
            "name": "CountPerValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    values: Optional[ExternalDataArray] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
