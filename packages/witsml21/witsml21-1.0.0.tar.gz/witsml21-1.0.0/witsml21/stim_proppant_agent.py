from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.area_per_mass_measure import AreaPerMassMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.proppant_agent_kind import ProppantAgentKind
from witsml21.stim_iso13503_2_properties import StimIso135032Properties
from witsml21.stim_iso13503_5_point import StimIso135035Point
from witsml21.stim_material import StimMaterial

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimProppantAgent(StimMaterial):
    """
    Captures a description of a proppant used in a stimulation job.

    :ivar friction_coefficient_laminar: Laminar flow friction
        coefficient.
    :ivar friction_coefficient_turbulent: Turbulent flow friction
        coefficient.
    :ivar mass_absorption_coefficient: Characterizes how easily
        radiation passes through a material. This can be used to compute
        the concentration of proppant in a slurry using a densitometer.
    :ivar mesh_size_high: High value of sieve mesh size: for 40/70 sand,
        this value is 70.
    :ivar mesh_size_low: Low value of sieve mesh size: for 40/70 sand,
        this value is 40.
    :ivar unconfined_compressive_strength: The unconfined compressive
        strength of the proppant.
    :ivar proppant_agent_kind: Proppant type or function.
    :ivar iso13503_2_properties:
    :ivar iso13503_5_point:
    """
    friction_coefficient_laminar: Optional[float] = field(
        default=None,
        metadata={
            "name": "FrictionCoefficientLaminar",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    friction_coefficient_turbulent: Optional[float] = field(
        default=None,
        metadata={
            "name": "FrictionCoefficientTurbulent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mass_absorption_coefficient: Optional[AreaPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "MassAbsorptionCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mesh_size_high: Optional[int] = field(
        default=None,
        metadata={
            "name": "MeshSizeHigh",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_inclusive": 0,
        }
    )
    mesh_size_low: Optional[int] = field(
        default=None,
        metadata={
            "name": "MeshSizeLow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_inclusive": 0,
        }
    )
    unconfined_compressive_strength: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "UnconfinedCompressiveStrength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    proppant_agent_kind: Optional[ProppantAgentKind] = field(
        default=None,
        metadata={
            "name": "ProppantAgentKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    iso13503_2_properties: List[StimIso135032Properties] = field(
        default_factory=list,
        metadata={
            "name": "ISO13503_2Properties",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    iso13503_5_point: List[StimIso135035Point] = field(
        default_factory=list,
        metadata={
            "name": "ISO13503_5Point",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
