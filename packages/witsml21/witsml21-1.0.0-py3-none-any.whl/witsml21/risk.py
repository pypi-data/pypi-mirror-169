from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_object import AbstractObject
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_measure import LengthMeasure
from witsml21.measured_depth import MeasuredDepth
from witsml21.risk_affected_personnel import RiskAffectedPersonnel
from witsml21.risk_category import RiskCategory
from witsml21.risk_sub_category import RiskSubCategory
from witsml21.risk_type import RiskType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Risk(AbstractObject):
    """Risk Schema.

    Used to provide a central location for capturing risk information
    about the well design and other well-related data objects.

    :ivar type: The type of risk.
    :ivar category: The category of risk.
    :ivar sub_category: The sub category of risk.
    :ivar extend_category: Custom string to further categorize the risk.
    :ivar affected_personnel: The personnel affected by the risk.
    :ivar dtim_start: Date and time that activities (related to the
        risk) started.
    :ivar dtim_end: Date and time that activities (related to the risk)
        were completed.
    :ivar md_hole_start: Measured Depth at the start of the activity.
    :ivar md_hole_end: Measured Depth at the end of the activity.
    :ivar tvd_hole_start: True vertical depth at the start of the
        activity.
    :ivar tvd_hole_end: True vertical depth at the end of the activity.
    :ivar md_bit_start: Measured depth of the bit at the start of the
        activity.
    :ivar md_bit_end: Measured depth of the bit at the end of the
        activity.
    :ivar dia_hole: Hole diameter.
    :ivar severity_level: Severity level of the risk. Values of 1
        through 5, with 1 being the lowest risk level.
    :ivar probability_level: Probability level of the risk occurring.
        Values of 1 through 5, with 1 being the lowest probability.
    :ivar summary: Summary description of the risk.
    :ivar details: Complete description of the risk.
    :ivar identification: Details for identifying the risk.
    :ivar contingency: Plan of action if the risk materializes.
    :ivar mitigation: Plan of action to ensure the risk does not
        materialize.
    :ivar object_reference:
    :ivar wellbore:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    type: Optional[RiskType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        }
    )
    category: Optional[RiskCategory] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "required": True,
        }
    )
    sub_category: Optional[RiskSubCategory] = field(
        default=None,
        metadata={
            "name": "SubCategory",
            "type": "Element",
        }
    )
    extend_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExtendCategory",
            "type": "Element",
            "max_length": 64,
        }
    )
    affected_personnel: List[RiskAffectedPersonnel] = field(
        default_factory=list,
        metadata={
            "name": "AffectedPersonnel",
            "type": "Element",
        }
    )
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    md_hole_start: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdHoleStart",
            "type": "Element",
        }
    )
    md_hole_end: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdHoleEnd",
            "type": "Element",
        }
    )
    tvd_hole_start: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdHoleStart",
            "type": "Element",
        }
    )
    tvd_hole_end: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdHoleEnd",
            "type": "Element",
        }
    )
    md_bit_start: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdBitStart",
            "type": "Element",
        }
    )
    md_bit_end: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdBitEnd",
            "type": "Element",
        }
    )
    dia_hole: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaHole",
            "type": "Element",
        }
    )
    severity_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeverityLevel",
            "type": "Element",
            "min_inclusive": "0",
            "max_inclusive": "8",
            "pattern": r".+",
        }
    )
    probability_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProbabilityLevel",
            "type": "Element",
            "min_inclusive": "0",
            "max_inclusive": "8",
            "pattern": r".+",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "name": "Summary",
            "type": "Element",
            "max_length": 2000,
        }
    )
    details: Optional[str] = field(
        default=None,
        metadata={
            "name": "Details",
            "type": "Element",
            "max_length": 2000,
        }
    )
    identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "Identification",
            "type": "Element",
            "max_length": 2000,
        }
    )
    contingency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Contingency",
            "type": "Element",
            "max_length": 2000,
        }
    )
    mitigation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Mitigation",
            "type": "Element",
            "max_length": 2000,
        }
    )
    object_reference: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "ObjectReference",
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
