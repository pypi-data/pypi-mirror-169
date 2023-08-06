from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.mass_per_length_measure import MassPerLengthMeasure
from witsml21.md_interval import MdInterval
from witsml21.volume_per_length_measure import VolumePerLengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimTubular:
    """
    In a production enhancement job, this item constitutes the data for a
    tubular in the hole.

    :ivar type: The type of tubular (e.g., casing, tubing, liner,
        packer, open hole, other).
    :ivar id: The inside diameter of the tubular used.
    :ivar od: The outside diameter of the tubular used.
    :ivar weight: The weight per length of the tubular.
    :ivar tubular_md_interval: Measured depth interval over which the
        tubular was used.
    :ivar tubular_tvd_interval: True vertical depth interval over which
        the tubular was used.
    :ivar volume_factor: The volume per length of the tubular.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of StimTubular.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    weight: Optional[MassPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "TubularMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular_tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "TubularTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    volume_factor: Optional[VolumePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeFactor",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
