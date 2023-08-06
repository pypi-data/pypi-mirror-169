from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.name_tag import NameTag
from witsml21.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Centrifuge:
    """
    Rig Centrifuge Schema.

    :ivar manufacturer: Pointer to a BusinessAssociate representing the
        manufacturer or supplier of the item.
    :ivar model: Manufacturer's designated model.
    :ivar dtim_install: Date and time the centrifuge was installed.
    :ivar dtim_remove: Date and time the centrifuge was removed.
    :ivar type: Description for the type of object.
    :ivar cap_flow: Maximum pump rate at which the unit efficiently
        operates.
    :ivar owner: Pointer to a BusinessAssociate representing the
        contractor/owner.
    :ivar name_tag: An identification tag for the centrifuge. A serial
        number is a type of identification tag; however, some tags
        contain many pieces of information.This element only identifies
        the tag and does not describe the contents.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Centrifuge.
    """
    manufacturer: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    dtim_install: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimInstall",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_remove: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimRemove",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cap_flow: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "CapFlow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    owner: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Owner",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    name_tag: List[NameTag] = field(
        default_factory=list,
        metadata={
            "name": "NameTag",
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
