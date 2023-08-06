from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.abstract_object import AbstractObject
from witsml21.logging_method import LoggingMethod
from witsml21.logging_tool_class import LoggingToolType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class LoggingToolKind(AbstractObject):
    """
    Common information about a kind of logging tool, such as a specific model
    of logging tool from a logging company.

    :ivar logging_company_name: Name of the logging company that
        operates this kind of logging tool.
    :ivar logging_company_code: The RP66 organization code assigned to
        the logging company. The list is available at
        http://www.energistics.org/geosciences/geology-
        standards/rp66-organization-codes
    :ivar identifier: The tool code or tool model that uniquely
        identifies the kind of logging tool.
    :ivar group_identifier: The tool group or tool series for the kind
        of logging tool.
    :ivar marketing_name: The marketing name for the kind of logging
        tool.
    :ivar class_value: The class for this kind of logging tool such as
        AC (Acoustic) or GR (Gamma Ray).
    :ivar class_description: An optional description of the class for
        this kind of logging tool. This should be populated when the
        class is an extension value.
    :ivar logging_method: The logging method (e.g., LWD, MWD, wireline)
        for this kind of logging tool.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    logging_company_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoggingCompanyName",
            "type": "Element",
            "required": True,
            "max_length": 256,
        }
    )
    logging_company_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoggingCompanyCode",
            "type": "Element",
            "required": True,
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    group_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "GroupIdentifier",
            "type": "Element",
            "max_length": 64,
        }
    )
    marketing_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarketingName",
            "type": "Element",
            "max_length": 64,
        }
    )
    class_value: Optional[Union[LoggingToolType, str]] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    class_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassDescription",
            "type": "Element",
            "max_length": 256,
        }
    )
    logging_method: Optional[LoggingMethod] = field(
        default=None,
        metadata={
            "name": "LoggingMethod",
            "type": "Element",
        }
    )
