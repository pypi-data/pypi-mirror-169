from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_growing_object import AbstractMdGrowingObject
from witsml21.data_object_reference import DataObjectReference
from witsml21.mud_log_parameter import MudLogParameter
from witsml21.mudlog_report_interval import MudlogReportInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudLogReport(AbstractMdGrowingObject):
    """
    Details of wellbore geology intervals, drilling parameters, chromatograph,
    mud gas, etc., data within an MD interval.

    :ivar mud_log_company: Pointer to a BusinessAssociate representing
        the company recording the information.
    :ivar mud_log_engineers: Concatenated names of the mudloggers
        constructing the log.
    :ivar mud_log_geologists: Concatenated names of the geologists
        constructing the log.
    :ivar wellbore:
    :ivar wellbore_geology:
    :ivar related_log:
    :ivar mudlog_report_interval:
    :ivar parameter:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    mud_log_company: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "MudLogCompany",
            "type": "Element",
        }
    )
    mud_log_engineers: Optional[str] = field(
        default=None,
        metadata={
            "name": "MudLogEngineers",
            "type": "Element",
            "max_length": 2000,
        }
    )
    mud_log_geologists: Optional[str] = field(
        default=None,
        metadata={
            "name": "MudLogGeologists",
            "type": "Element",
            "max_length": 2000,
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
    wellbore_geology: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WellboreGeology",
            "type": "Element",
        }
    )
    related_log: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "RelatedLog",
            "type": "Element",
        }
    )
    mudlog_report_interval: List[MudlogReportInterval] = field(
        default_factory=list,
        metadata={
            "name": "MudlogReportInterval",
            "type": "Element",
        }
    )
    parameter: List[MudLogParameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
        }
    )
