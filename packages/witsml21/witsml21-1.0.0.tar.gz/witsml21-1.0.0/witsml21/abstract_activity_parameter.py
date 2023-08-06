from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_parameter_key import AbstractParameterKey

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractActivityParameter:
    """
    General parameter value used in one instance of activity.

    :ivar title: Name of the parameter, used to identify it in the
        activity. Must have an equivalent in the activity descriptor
        parameters.
    :ivar index: When parameter is an array, used to indicate the index
        in the array
    :ivar selection: Textual description about how this parameter was
        selected.
    :ivar is_uncertain: Used to indicate that a parameter is not
        necessarily deterministic but can be replaced by a stochastic
        method to generate a value.
    :ivar key:
    """
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    selection: Optional[str] = field(
        default=None,
        metadata={
            "name": "Selection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    is_uncertain: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsUncertain",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    key: List[AbstractParameterKey] = field(
        default_factory=list,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
