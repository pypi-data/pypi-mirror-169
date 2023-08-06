from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ChannelOsduintegration:
    """
    Information about a Channel that is relevant for OSDU integration but does
    not have a natural place in a Channel object.

    :ivar channel_quality: The quality of the channel.
    :ivar intermediary_service_company: Pointer to a BusinessAssociate
        that represents the company who engaged the service company
        (ServiceCompany) to perform the logging.
    :ivar is_regular: Boolean property indicating the sampling mode of
        the primary index. True means all channel data values are
        regularly spaced (see NominalSamplingInterval); false means
        irregular or discrete sample spacing.
    :ivar zero_time: Optional time reference for time-based primary
        indexes. The ISO date time string representing zero time. Not to
        be confused with seismic travel time zero.
    :ivar channel_business_value: The business value of the channel.
    :ivar channel_main_family: The Geological Physical Quantity measured
        by the channel such as porosity.
    :ivar channel_family: The detailed Geological Physical Quantity
        measured by the channel such as neutron porosity.
    """
    class Meta:
        name = "ChannelOSDUIntegration"

    channel_quality: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChannelQuality",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
    is_regular: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRegular",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    channel_business_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChannelBusinessValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    channel_main_family: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChannelMainFamily",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    channel_family: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChannelFamily",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
