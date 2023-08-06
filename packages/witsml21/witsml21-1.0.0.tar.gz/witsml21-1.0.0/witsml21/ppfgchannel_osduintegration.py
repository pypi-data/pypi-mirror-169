from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PpfgchannelOsduintegration:
    """
    Information about a PPFGChannel that is relevant for OSDU integration but
    does not have a natural place in a PPFGChannel object.

    :ivar record_date: The date that the PPFG channel was created by the
        PPFG practitioner or contractor.
    """
    class Meta:
        name = "PPFGChannelOSDUIntegration"

    record_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecordDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
