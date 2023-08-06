from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReferencePointVerticalDepth(AbstractVerticalDepth):
    reference_point: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
