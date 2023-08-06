from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportLithShowInfo:
    """
    General information about the lithology and shows in an interval
    encountered during the drill report period.

    :ivar dtim: Date and time that the well test was completed.
    :ivar show_md_interval: Measured depth interval over which the show
        appears.
    :ivar show_tvd_interval: True vertical depth interval over which the
        show appears.
    :ivar show: A textual description of any shows in the interval.
    :ivar lithology: A geological/lithological description/evaluation of
        the interval.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        DrillReportLithShowInfo
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    show_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "ShowMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    show_tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "ShowTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    show: Optional[str] = field(
        default=None,
        metadata={
            "name": "Show",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    lithology: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lithology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
