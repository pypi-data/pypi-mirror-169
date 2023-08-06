from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_object import AbstractObject
from witsml21.data_object_reference import DataObjectReference
from witsml21.error_propagation_mode import ErrorPropagationMode
from witsml21.gyro_mode import GyroMode
from witsml21.measure_class import MeasureType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ErrorTerm(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    gyro_mode: Optional[GyroMode] = field(
        default=None,
        metadata={
            "name": "GyroMode",
            "type": "Element",
        }
    )
    measure_class: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "MeasureClass",
            "type": "Element",
        }
    )
    propagation_mode: Optional[ErrorPropagationMode] = field(
        default=None,
        metadata={
            "name": "PropagationMode",
            "type": "Element",
            "required": True,
        }
    )
    weighting_function: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WeightingFunction",
            "type": "Element",
            "required": True,
        }
    )
