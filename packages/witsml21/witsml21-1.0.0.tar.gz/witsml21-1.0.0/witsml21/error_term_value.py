from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.generic_measure import GenericMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ErrorTermValue:
    """
    :ivar magnitude: Business Rule : The unconstrained uom of the
        magnitude is actually constrained by the MeasureClass set to the
        associated ErrorTerm.
    :ivar mean_value: Business Rules : - The unconstrained uom of the
        mean value is actually constrained by the MeasureClass set to
        the associated ErrorTerm. - If propagation mode is set to 'B'
        then MeanValue must exist
    :ivar error_term:
    """
    magnitude: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "Magnitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    mean_value: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "MeanValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    error_term: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ErrorTerm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
