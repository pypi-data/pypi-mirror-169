from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.abstract_object import AbstractObject
from witsml21.collection_kind import CollectionKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DataobjectCollection(AbstractObject):
    """Allows multiple data objects to be grouped together into a collection.

    The relationships (between the data objects and the collection) are
    specified and managed using the SingleCollectionAssociation.

    :ivar kind: Indicates the semantic of the collection. It is an
        extensible enumeration. So it may be one of the enumerations
        listed in CollectionKind or an implemenation may specify its own
        kind using CollectionKindExt.
    :ivar homogeneous_datatype: Boolean flag. If true all data objects
        in the collection are of the same Energistics data type
        (EXAMPLE: All wellbores or all horizons).
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    kind: Optional[Union[CollectionKind, str]] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    homogeneous_datatype: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HomogeneousDatatype",
            "type": "Element",
        }
    )
