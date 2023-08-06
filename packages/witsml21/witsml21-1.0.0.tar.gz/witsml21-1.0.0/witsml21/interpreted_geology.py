from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_growing_object import AbstractMdGrowingObject
from witsml21.data_object_reference import DataObjectReference
from witsml21.interpreted_geology_interval import InterpretedGeologyInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class InterpretedGeology(AbstractMdGrowingObject):
    """A container object for zero or more InterpretedGeologyInterval objects.

    The container references a specific wellbore, a depth interval, a
    growing object status, and a collection of interpreted geology
    intervals. These values are manually entered per sample by the
    wellsite geologist or mud logger as an interpretation of the actual
    lithology sequence along the length of the wellbore by correlating
    the percentage lithologies observed in the cuttings samples along
    with other data (typically the drill rate and gamma ray curves), to
    estimate the location of the boundaries between the different
    lithology types. This analysis creates a sequence of individual
    lithologies along the wellbore. Therefore, InterpretedGeology
    typically contains a single lithology element for each interval that
    captures the detailed geological description of the lithology.

    :ivar interpreted_geology_interval:
    :ivar wellbore: Business Rule: This MUST point to the same wellbore
        that the Wellbore element on the containing WellboreGeology
        object points to.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    interpreted_geology_interval: List[InterpretedGeologyInterval] = field(
        default_factory=list,
        metadata={
            "name": "InterpretedGeologyInterval",
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
