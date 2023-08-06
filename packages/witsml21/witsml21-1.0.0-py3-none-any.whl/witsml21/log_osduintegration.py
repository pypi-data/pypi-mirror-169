from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class LogOsduintegration:
    """
    Information about a Log that is relevant for OSDU integration but does not
    have a natural place in a Log object.

    :ivar log_version: The log version. Distinct from objectVersion.
    :ivar zero_time: Optional time reference for time-based primary
        indexes. The ISO date time string representing zero time. Not to
        be confused with seismic travel time zero.
    :ivar frame_identifier: For multi-frame or multi-section files, this
        identifier defines the source frame in the file. If the
        identifier is an index number the index starts with zero and is
        converted to a string for this property.
    :ivar is_regular: Boolean property indicating the sampling mode of
        the primary index. True means all channel data values are
        regularly spaced (see NominalSamplingInterval); false means
        irregular or discrete sample spacing.
    :ivar intermediary_service_company: Pointer to a BusinessAssociate
        that represents the company who engaged the service company
        (ServiceCompany) to perform the logging.
    """
    class Meta:
        name = "LogOSDUIntegration"

    log_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogVersion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    zero_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZeroTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    frame_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrameIdentifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    is_regular: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRegular",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
