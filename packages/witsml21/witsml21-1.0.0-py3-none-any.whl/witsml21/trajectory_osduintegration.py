from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TrajectoryOsduintegration:
    """
    Information about a Trajectory that is relevant for OSDU integration but
    does not have a natural place in a Trajectory object.

    :ivar active_indicator: Active Survey Indicator. Distinct from
        ActiveStatus on Trajectory.
    :ivar applied_operation: The audit trail of operations applied to
        the station coordinates from the original state to the current
        state. The list may contain operations applied prior to
        ingestion as well as the operations applied to produce the
        Wgs84Coordinates. The text elements refer to ESRI style CRS and
        Transformation names, which may have to be translated to EPSG
        standard names.
    :ivar intermediary_service_company: Pointer to a BusinessAssociate
        that represents the company who engaged the service company
        (ServiceCompany) to perform the surveying.
    :ivar survey_tool_type: The type of tool or equipment used to
        acquire this Directional Survey.
    :ivar trajectory_version: The version of the wellbore survey
        deliverable received from the service provider - as given by
        this provider. Distinct from objectVersion.
    """
    class Meta:
        name = "TrajectoryOSDUIntegration"

    active_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActiveIndicator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    applied_operation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AppliedOperation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 256,
        }
    )
    intermediary_service_company: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IntermediaryServiceCompany",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    survey_tool_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurveyToolType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 256,
        }
    )
    trajectory_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrajectoryVersion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
