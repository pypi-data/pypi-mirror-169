from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.geology_type import GeologyType
from witsml21.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class GeologyFeature:
    """
    Geology features found in the location of the borehole string.

    :ivar name: Name of the feature.
    :ivar geology_type: Aquifer or reservoir.
    :ivar feature_md_interval: Measured depth interval for this feature.
    :ivar feature_tvd_interval: True vertical depth interval for this
        feature.
    :ivar geologic_unit_interpretation: Reference to a RESQML geologic
        unit interpretation for this feature.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of GeologyFeature.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    geology_type: Optional[GeologyType] = field(
        default=None,
        metadata={
            "name": "GeologyType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    feature_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "FeatureMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    feature_tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "FeatureTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    geologic_unit_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "GeologicUnitInterpretation",
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
