from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.channel import Channel
from witsml21.ppfgchannel_osduintegration import PpfgchannelOsduintegration
from witsml21.ppfgdata_derivation import PpfgdataDerivation
from witsml21.ppfgdata_processing import PpfgdataProcessing
from witsml21.ppfgfamily import Ppfgfamily
from witsml21.ppfgfamily_mnemonic import PpfgfamilyMnemonic
from witsml21.ppfgmain_family import PpfgmainFamily
from witsml21.ppfgmodeled_lithology import PpfgmodeledLithology
from witsml21.ppfgtransform_model_type import PpfgtransformModelType
from witsml21.ppfguncertainty_class import PpfguncertaintyType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Ppfgchannel(Channel):
    """A channel object specific to pore pressure and fracture gradient
    modeling.

    It corresponds roughly to a PPFGDataSetCurve in OSDU.

    :ivar ppfgdata_processing_applied: An array of processing operations
        that have been applied to this channel's data. For example:
        'Smoothed', 'Calibrated', etc.
    :ivar ppfgderivation: Indicates how the PPFG data in the channel was
        derived.
    :ivar ppfgfamily: The PPFG Family of the PPFG quantity measured, for
        example 'Pore Pressure from Corrected Drilling Exponent'. An
        individual channel that belongs to a Main Family.
    :ivar ppfgfamily_mnemonic: The mnemonic of the PPFG Family.
    :ivar ppfgmain_family: The Main Family Type of the PPFG quantity
        measured, for example 'Pore Pressure'. Primarily used for high
        level data classification.
    :ivar ppfgmodeled_lithology: The lithology that this channel was
        modeled on. The assumption is that several different channels
        will be modeled, each for a specific lithology type, and during
        drilling, when it is known which lithologyy the well is
        currently in, users would refer to the channels modeled on the
        appropropriate type of lithology.
    :ivar ppfgtransform_model_type: The empirical calibrated model used
        for pressure calculations from a petrophysical channel (sonic or
        resistivity), for example 'Eaton' and 'Bowers',... .
    :ivar ppfguncertainty_class: The uncertainty class for the channel,
        for example 'most likely' or 'p50'.
    :ivar ppfgchannel_osduintegration: Information about a PPFGChannel
        that is relevant for OSDU integration but does not have a
        natural place in a PPFGChannel object.
    """
    class Meta:
        name = "PPFGChannel"
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    ppfgdata_processing_applied: List[Union[PpfgdataProcessing, str]] = field(
        default_factory=list,
        metadata={
            "name": "PPFGDataProcessingApplied",
            "type": "Element",
            "pattern": r".*:.*",
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
    ppfgfamily: Optional[Union[Ppfgfamily, str]] = field(
        default=None,
        metadata={
            "name": "PPFGFamily",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    ppfgfamily_mnemonic: Optional[Union[PpfgfamilyMnemonic, str]] = field(
        default=None,
        metadata={
            "name": "PPFGFamilyMnemonic",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    ppfgmain_family: Optional[Union[PpfgmainFamily, str]] = field(
        default=None,
        metadata={
            "name": "PPFGMainFamily",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    ppfgmodeled_lithology: Optional[Union[PpfgmodeledLithology, str]] = field(
        default=None,
        metadata={
            "name": "PPFGModeledLithology",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    ppfgtransform_model_type: Optional[Union[PpfgtransformModelType, str]] = field(
        default=None,
        metadata={
            "name": "PPFGTransformModelType",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    ppfguncertainty_class: Optional[Union[PpfguncertaintyType, str]] = field(
        default=None,
        metadata={
            "name": "PPFGUncertaintyClass",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    ppfgchannel_osduintegration: Optional[PpfgchannelOsduintegration] = field(
        default=None,
        metadata={
            "name": "PPFGChannelOSDUIntegration",
            "type": "Element",
        }
    )
