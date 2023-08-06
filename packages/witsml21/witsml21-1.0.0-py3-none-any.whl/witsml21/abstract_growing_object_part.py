from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractGrowingObjectPart:
    """
    :ivar creation: Date and time the document was created in the source
        application or, if that information is not available, when it
        was saved to the file. This is the equivalent of the ISO 19115
        CI_Date where the CI_DateTypeCode = "creation" Format: YYYY-MM-
        DDThh:mm:ssZ[+/-]hh:mm Legacy DCGroup - created
    :ivar last_update: An ISO 19115 EIP-derived set of metadata attached
        to all specializations of AbstractObject to ensure the
        traceability of each individual independent (top level) element.
    :ivar extension_name_value:
    :ivar uid: Unique identifier for this instance of a growing part.
    :ivar object_version:
    """
    creation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    last_update: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastUpdate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    extension_name_value: Optional[ExtensionNameValue] = field(
        default=None,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    object_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "objectVersion",
            "type": "Attribute",
            "max_length": 64,
        }
    )
