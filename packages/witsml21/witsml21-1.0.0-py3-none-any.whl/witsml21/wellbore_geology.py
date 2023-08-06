from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_active_object import AbstractActiveObject
from witsml21.cuttings_geology import CuttingsGeology
from witsml21.data_object_reference import DataObjectReference
from witsml21.interpreted_geology import InterpretedGeology
from witsml21.md_interval import MdInterval
from witsml21.show_evaluation import ShowEvaluation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreGeology(AbstractActiveObject):
    """
    The transferrable class of the WellboreGeology object.

    :ivar md_interval: [maintained by the server] The interval that
        contains the minimum and maximum measured depths for all
        wellbore geology types under this wellbore geology entry.
    :ivar wellbore:
    :ivar cuttings_geology: Business Rule: This MUST point to the same
        wellbore that the Wellbore element on the containing
        WellboreGeology object points to.
    :ivar interpreted_geology:
    :ivar show_evaluation:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "required": True,
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
    cuttings_geology: Optional[CuttingsGeology] = field(
        default=None,
        metadata={
            "name": "CuttingsGeology",
            "type": "Element",
        }
    )
    interpreted_geology: Optional[InterpretedGeology] = field(
        default=None,
        metadata={
            "name": "InterpretedGeology",
            "type": "Element",
        }
    )
    show_evaluation: Optional[ShowEvaluation] = field(
        default=None,
        metadata={
            "name": "ShowEvaluation",
            "type": "Element",
        }
    )
