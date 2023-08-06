from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_growing_object import AbstractMdGrowingObject
from witsml21.cuttings_geology_interval import CuttingsGeologyInterval
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CuttingsGeology(AbstractMdGrowingObject):
    """Container for Cuttings Lithology items.

    The mud logger at the wellsite takes regular samples of drilled
    cuttings while the well is being drilled and examines the cuttings
    to determine the rock types (lithologies) present in each sample.
    The cuttings samples will typically contain a mix of different
    lithologies in each sample because there may have been multiple rock
    types that were drilled within the sample depth interval and there
    can also be mixing of cuttings as they travel up the wellbore and
    are collected on the shakers. CuttingsGeology therefore will
    typically contain multiple lithology elements for each interval so
    that the percentages of each lithology in the sample along with the
    more detailed geological description can be recorded.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    cuttings_geology_interval: List[CuttingsGeologyInterval] = field(
        default_factory=list,
        metadata={
            "name": "CuttingsGeologyInterval",
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
