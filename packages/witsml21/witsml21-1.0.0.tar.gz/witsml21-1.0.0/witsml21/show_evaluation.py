from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_growing_object import AbstractMdGrowingObject
from witsml21.data_object_reference import DataObjectReference
from witsml21.show_evaluation_interval import ShowEvaluationInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ShowEvaluation(AbstractMdGrowingObject):
    """A container object for zero or more ShowEvaluationInterval objects.

    The container references a specific wellbore, a depth interval, a
    growing object status, and a collection of show evaluation
    intervals. In a similar way to the InterpretedGeology, these are
    manually entered by the wellsite geologist or mud logger as an
    interpretation of the hydrocarbon show along the wellbore, based on
    the raw readings from one or more show analyses of individual show
    tests on cuttings samples.

    :ivar show_evaluation_interval:
    :ivar wellbore: Business Rule: This MUST point to the same wellbore
        that the Wellbore element on the containing WellboreGeology
        object points to.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    show_evaluation_interval: List[ShowEvaluationInterval] = field(
        default_factory=list,
        metadata={
            "name": "ShowEvaluationInterval",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
