from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ShakerScreen:
    """
    Operations Shaker Screen Component Schema.

    :ivar dtim_start: Date and time that activities started.
    :ivar dtim_end: Date and time activities were completed.
    :ivar num_deck: Deck number the mesh is installed on.
    :ivar mesh_x: Mesh size in the X direction.
    :ivar mesh_y: Mesh size in the Y direction.
    :ivar manufacturer: Pointer to a BusinessAssociate representing the
        manufacturer or supplier of the item.
    :ivar model: Manufacturers designated model.
    :ivar cut_point: Shaker screen cut point, which is the maximum size
        cuttings that will pass through the screen.
    """
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    num_deck: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumDeck",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mesh_x: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MeshX",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mesh_y: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MeshY",
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
    model: Optional[str] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cut_point: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "CutPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
