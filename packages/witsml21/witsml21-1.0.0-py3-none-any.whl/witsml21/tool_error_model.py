from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.abstract_object import AbstractObject
from witsml21.authorization import Authorization
from witsml21.correction_considered import CorrectionConsidered
from witsml21.data_object_reference import DataObjectReference
from witsml21.error_term_value import ErrorTermValue
from witsml21.gyro_tool_configuration import GyroToolConfiguration
from witsml21.misalignment_mode import MisalignmentMode
from witsml21.operating_condition import OperatingCondition
from witsml21.operating_constraints import OperatingConstraints
from witsml21.tool_kind import ToolKind
from witsml21.tool_sub_kind import ToolSubKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ToolErrorModel(AbstractObject):
    """
    :ivar application:
    :ivar source:
    :ivar tool_kind:
    :ivar tool_sub_kind:
    :ivar operating_condition:
    :ivar survey_run_date_end: QC with Trajectory date end
    :ivar correction_considered:
    :ivar survey_run_date_start: QC with Trajectory date end
    :ivar misalignment_mode: Because software handles it (possibility
    :ivar operating_constraints:
    :ivar authorization:
    :ivar error_term_value:
    :ivar gyro_tool_configuration:
    :ivar replaces:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    application: Optional[str] = field(
        default=None,
        metadata={
            "name": "Application",
            "type": "Element",
            "max_length": 2000,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "max_length": 2000,
        }
    )
    tool_kind: Optional[ToolKind] = field(
        default=None,
        metadata={
            "name": "ToolKind",
            "type": "Element",
        }
    )
    tool_sub_kind: List[Union[ToolSubKind, str]] = field(
        default_factory=list,
        metadata={
            "name": "ToolSubKind",
            "type": "Element",
            "min_occurs": 1,
            "pattern": r".*:.*",
        }
    )
    operating_condition: List[Union[OperatingCondition, str]] = field(
        default_factory=list,
        metadata={
            "name": "OperatingCondition",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    survey_run_date_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurveyRunDateEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    correction_considered: List[Union[CorrectionConsidered, str]] = field(
        default_factory=list,
        metadata={
            "name": "CorrectionConsidered",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    survey_run_date_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurveyRunDateStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    misalignment_mode: Optional[MisalignmentMode] = field(
        default=None,
        metadata={
            "name": "MisalignmentMode",
            "type": "Element",
            "required": True,
        }
    )
    operating_constraints: Optional[OperatingConstraints] = field(
        default=None,
        metadata={
            "name": "OperatingConstraints",
            "type": "Element",
        }
    )
    authorization: Optional[Authorization] = field(
        default=None,
        metadata={
            "name": "Authorization",
            "type": "Element",
            "required": True,
        }
    )
    error_term_value: List[ErrorTermValue] = field(
        default_factory=list,
        metadata={
            "name": "ErrorTermValue",
            "type": "Element",
        }
    )
    gyro_tool_configuration: Optional[GyroToolConfiguration] = field(
        default=None,
        metadata={
            "name": "GyroToolConfiguration",
            "type": "Element",
        }
    )
    replaces: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Replaces",
            "type": "Element",
        }
    )
