from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.channel_set import ChannelSet
from witsml21.data_object_reference import DataObjectReference
from witsml21.ppfgchannel_set_osduintegration import PpfgchannelSetOsduintegration
from witsml21.ppfgdata_derivation import PpfgdataDerivation
from witsml21.ppfgtectonic_setting import PpfgtectonicSetting

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PpfgchannelSet(ChannelSet):
    """A channel set object specific to pore pressure and fracture gradient
    modeling.

    It corresponds roughly to a PPFGDataSet in OSDU.

    :ivar ppfgcomment: Open comments from the PPFG calculation team.
    :ivar ppfgderivation: Nominal indication of how how the PPFG data in
        the channel set was derived. Individual channels may have
        different derivations.
    :ivar ppfggauge_type: Free text to describe the type of gauge used
        for the pressure measurement.
    :ivar ppfgoffset_wellbore: Offset Wellbores included in the context
        and calculations of this PPFG channel set.
    :ivar ppfgtectonic_setting: Tectonic Scenario Setting for Planning
        and Pore Pressure Practitioners. Built into interpretive curves.
        Can be, for example 'Strike Slip'.
    :ivar ppfgchannel_set_osduintegration: Information about a
        PPFGChannelSet that is relevant for OSDU integration but does
        not have a natural place in a PPFGChannelSet object.
    """
    class Meta:
        name = "PPFGChannelSet"
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    ppfgcomment: Optional[str] = field(
        default=None,
        metadata={
            "name": "PPFGComment",
            "type": "Element",
            "max_length": 2000,
        }
    )
    ppfgderivation: Optional[Union[PpfgdataDerivation, str]] = field(
        default=None,
        metadata={
            "name": "PPFGDerivation",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    ppfggauge_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PPFGGaugeType",
            "type": "Element",
            "max_length": 64,
        }
    )
    ppfgoffset_wellbore: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "PPFGOffsetWellbore",
            "type": "Element",
        }
    )
    ppfgtectonic_setting: Optional[Union[PpfgtectonicSetting, str]] = field(
        default=None,
        metadata={
            "name": "PPFGTectonicSetting",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    ppfgchannel_set_osduintegration: Optional[PpfgchannelSetOsduintegration] = field(
        default=None,
        metadata={
            "name": "PPFGChannelSetOSDUIntegration",
            "type": "Element",
        }
    )
