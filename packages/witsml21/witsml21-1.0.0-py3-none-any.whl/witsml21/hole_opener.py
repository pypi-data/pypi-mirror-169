from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.hole_opener_type import HoleOpenerType
from witsml21.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class HoleOpener:
    """Hole Opener Component Schema.

    Describes the hole-opener tool (often called a ‘reamer’) used on the
    tubular string.

    :ivar type_hole_opener: Under reamer or fixed blade.
    :ivar num_cutter: Number of cutters on the tool.
    :ivar manufacturer: Pointer to a BusinessAssociate representing the
        manufacturer or supplier of the tool.
    :ivar dia_hole_opener: Diameter of the reamer.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    """
    type_hole_opener: Optional[HoleOpenerType] = field(
        default=None,
        metadata={
            "name": "TypeHoleOpener",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_cutter: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumCutter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    manufacturer: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_hole_opener: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaHoleOpener",
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
