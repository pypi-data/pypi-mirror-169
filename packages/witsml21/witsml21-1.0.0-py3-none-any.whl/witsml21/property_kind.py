from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.abstract_object import AbstractObject
from witsml21.data_object_reference import DataObjectReference
from witsml21.quantity_class_kind import QuantityTypeKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PropertyKind(AbstractObject):
    """Property kinds carry the semantics of property values.

    They are used to identify if the values are, for example,
    representing porosity, length, stress tensor, etc. Energistics
    provides a list of standard property kind that represent the basis
    for the commonly used properties in the E&amp;P subsurface workflow.

    :ivar is_abstract: This boolean indicates whether the PropertyKind
        should be used as a real property or not. If the Is Abstract
        flag is set, then this entry should be used only as the parent
        of a real property. For example, the PropertyKind of "force per
        length" shouldn't be used directly, as it is really just a
        description of some units of measure. This entry should only be
        used as the parent of the real physical property "surface
        tension".
    :ivar deprecation_date: Date at which this property dictionary entry
        must no longer be used. Files generated before this date would
        have used this entry so it is left here for reference. A null
        value means the property kind is still valid.
    :ivar quantity_class: A reference to the name of a quantity class in
        the Energistics Unit of Measure Dictionary. If there is no match
        in the Energistics Unit of Measure Dictionary, then this
        attribute is purely for human information.
    :ivar parent: Indicates the parent of this property kind. BUSINESS
        RULE : Only the top root abstract property kind has not to
        define a parent property kind.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    is_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAbstract",
            "type": "Element",
            "required": True,
        }
    )
    deprecation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeprecationDate",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    quantity_class: Optional[Union[QuantityTypeKind, str]] = field(
        default=None,
        metadata={
            "name": "QuantityClass",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    parent: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
        }
    )
