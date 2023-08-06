from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_bottom_hole_temperature import AbstractBottomHoleTemperature
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.md_interval import MdInterval
from witsml21.measured_depth import MeasuredDepth

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportLogInfo:
    """
    General information about a log conducted during the drill report period.

    :ivar dtim: The date and time that the log was completed.
    :ivar run_number: Log run number. For measurement while drilling,
        this should be the bottom hole assembly number.
    :ivar service_company: Pointer to a BusinessAssociate representing
        the contractor who provided the service.
    :ivar logged_md_interval: Measured depth interval from the top to
        the base of the interval logged.
    :ivar logged_tvd_interval: True vertical depth interval from the top
        to the base of the interval logged.
    :ivar tool: A pointer to the logging tool kind for the logging tool.
    :ivar md_temp_tool: Measured depth to the temperature measurement
        tool.
    :ivar tvd_temp_tool: True vertical depth to the temperature
        measurement tool.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar bottom_hole_temperature:
    :ivar uid: Unique identifier for this instance of
        DrillReportLogInfo.
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
    run_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RunNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    service_company: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ServiceCompany",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    logged_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "LoggedMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    logged_tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "LoggedTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tool: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Tool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_temp_tool: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdTempTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_temp_tool: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdTempTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    bottom_hole_temperature: Optional[AbstractBottomHoleTemperature] = field(
        default=None,
        metadata={
            "name": "BottomHoleTemperature",
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
