from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.component_reference import ComponentReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure
from witsml21.time_measure import TimeMeasure
from witsml21.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PitVolume:
    """
    Pit Volume Component Schema.

    :ivar pit: This is a pointer to the corresponding pit on the rig
        containing the volume being described.
    :ivar dtim: Date and time the information is related to.
    :ivar vol_pit: Volume of fluid in the pit.
    :ivar dens_fluid: Density of fluid in the pit.
    :ivar desc_fluid: Description of the fluid in the pit.
    :ivar vis_funnel: Funnel viscosity (in seconds).
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of PitVolume.
    """
    pit: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "Pit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    vol_pit: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolPit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    dens_fluid: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    desc_fluid: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    vis_funnel: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "VisFunnel",
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
