from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.component_reference import ComponentReference
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class SourceTrajectoryStation:
    """A reference to a trajectoryStation in a wellbore.

    The trajectoryStation may be defined within the context of another
    wellbore. This value represents a foreign key from one element to
    another.

    :ivar station_reference: A pointer to the trajectoryStation within
        the parent trajectory. StationReference is a special case where
        WITSML only uses a UID for the pointer.The natural identity of a
        station is its physical characteristics (e.g., md).
    :ivar trajectory:
    """
    station_reference: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "StationReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
