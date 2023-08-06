from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.mass_per_mass_measure import MassPerMassMeasure
from witsml21.pressure_measure import PressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Iso135032CrushTestData:
    """
    Crush test data point.

    :ivar fines: Mass percentage of fines after being exposed to stress.
    :ivar stress: Stress measured at a point during a crush test.
    :ivar uid: Unique identifier for this instance of
        ISO13503_2CrushTestData.
    """
    class Meta:
        name = "ISO13503_2CrushTestData"

    fines: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Fines",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    stress: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Stress",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
