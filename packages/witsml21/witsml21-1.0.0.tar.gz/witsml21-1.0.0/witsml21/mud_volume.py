from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.mud_losses import MudLosses
from witsml21.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudVolume:
    """
    Operations Mud Volume Component Schema.

    :ivar vol_tot_mud_start: Total volume of mud at start of report
        interval (including pits and hole).
    :ivar vol_mud_dumped: Volume of mud dumped.
    :ivar vol_mud_received: Volume of mud received from mud warehouse.
    :ivar vol_mud_returned: Volume of mud returned to mud warehouse.
    :ivar vol_mud_built: Volume of mud built.
    :ivar vol_mud_string: Volume of mud contained within active string.
    :ivar vol_mud_casing: Volume of mud contained in casing annulus.
    :ivar vol_mud_hole: Volume of mud contained in the openhole annulus.
    :ivar vol_mud_riser: Volume of mud contained in riser section
        annulus.
    :ivar vol_tot_mud_end: Total volume of mud at the end of the report
        interval (including pits and hole).
    :ivar mud_losses:
    """
    vol_tot_mud_start: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolTotMudStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_mud_dumped: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudDumped",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_mud_received: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudReceived",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_mud_returned: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudReturned",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_mud_built: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudBuilt",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_mud_string: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudString",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_mud_casing: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudCasing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_mud_hole: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_mud_riser: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudRiser",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_tot_mud_end: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolTotMudEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mud_losses: Optional[MudLosses] = field(
        default=None,
        metadata={
            "name": "MudLosses",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
