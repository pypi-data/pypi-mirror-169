from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.authorization_status import AuthorizationStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Authorization:
    approval_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprovalAuthority",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    approved_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprovedBy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    approved_on: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprovedOn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    checked_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckedBy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    checked_on: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckedOn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    revision_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "RevisionComment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    revision_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RevisionDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    status: Optional[AuthorizationStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
