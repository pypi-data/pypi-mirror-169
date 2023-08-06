from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_activity_parameter import AbstractActivityParameter
from witsml21.abstract_object import AbstractObject
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Activity(AbstractObject):
    """
    Instance of a given activity.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    parent: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
        }
    )
    activity_descriptor: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ActivityDescriptor",
            "type": "Element",
            "required": True,
        }
    )
    parameter: List[AbstractActivityParameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "min_occurs": 1,
        }
    )
