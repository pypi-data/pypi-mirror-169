from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TubularUmbilicalOsduintegration:
    """
    Information about a TubularUmbilical that is relevant for OSDU integration
    but does not have a natural place in a TubularUmbilical.

    :ivar wellhead_outlet_key: The Wellhead Outlet the Umbilical is
        connected to.
    """
    class Meta:
        name = "TubularUmbilicalOSDUIntegration"

    wellhead_outlet_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellheadOutletKey",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
