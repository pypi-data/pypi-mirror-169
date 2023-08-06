from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_event_extension import AbstractEventExtension
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class LostCirculationExtension(AbstractEventExtension):
    """
    Information on lost circulation event.

    :ivar volume_lost: Volume lost
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    """
    volume_lost: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeLost",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
