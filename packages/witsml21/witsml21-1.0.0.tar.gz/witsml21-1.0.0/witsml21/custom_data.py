from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class CustomData:
    """WITSML - Custom or User Defined Element and Attributes Component Schema.
    Specify custom element, attributes, and types in the custom data area.

    :ivar any_element: Any element or attribute in any namespace. It is
        strongly recommended that all custom data definitions be added
        to a unique namespace.
    """
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
