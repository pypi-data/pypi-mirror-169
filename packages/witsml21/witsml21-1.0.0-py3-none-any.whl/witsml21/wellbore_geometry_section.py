from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_interval_growing_part import AbstractMdIntervalGrowingPart
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.data_object_reference import DataObjectReference
from witsml21.hole_casing_type import HoleCasingType
from witsml21.length_measure import LengthMeasure
from witsml21.mass_per_length_measure import MassPerLengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreGeometrySection(AbstractMdIntervalGrowingPart):
    """Wellbore Geometry Component Schema.

    Defines the "fixed" components in a wellbore. It does not define the
    "transient" drilling strings or the "hanging" production components.

    :ivar type_hole_casing: Type of fixed component.
    :ivar section_tvd_interval: True vertical depth interval for this
        wellbore geometry section.
    :ivar id_section: Inner diameter.
    :ivar od_section: Outer diameter. Only for casings and risers.
    :ivar wt_per_len: Weight per unit length for casing sections.
    :ivar grade: Material grade for the tubular section.
    :ivar curve_conductor: Curved conductor? Values are "true" (or "1")
        and "false" (or "0").
    :ivar dia_drift: The drift diameter is the inside diameter (ID) that
        the pipe manufacturer guarantees per specifications. Note that
        the nominal inside diameter is not the same as the drift
        diameter, but is always slightly larger. The drift diameter is
        used by the well planner to determine what size tools or casing
        strings can later be run through the casing, whereas the nominal
        inside diameter is used for fluid volume calculations, such as
        mud circulating times and cement slurry placement calculations.
        Source: www.glossary.oilfield.slb.com
    :ivar fact_fric: Friction factor.
    :ivar bha_run:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    type_hole_casing: Optional[HoleCasingType] = field(
        default=None,
        metadata={
            "name": "TypeHoleCasing",
            "type": "Element",
        }
    )
    section_tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "SectionTvdInterval",
            "type": "Element",
        }
    )
    id_section: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdSection",
            "type": "Element",
        }
    )
    od_section: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdSection",
            "type": "Element",
        }
    )
    wt_per_len: Optional[MassPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "WtPerLen",
            "type": "Element",
        }
    )
    grade: Optional[str] = field(
        default=None,
        metadata={
            "name": "Grade",
            "type": "Element",
            "max_length": 64,
        }
    )
    curve_conductor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CurveConductor",
            "type": "Element",
        }
    )
    dia_drift: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaDrift",
            "type": "Element",
        }
    )
    fact_fric: Optional[float] = field(
        default=None,
        metadata={
            "name": "FactFric",
            "type": "Element",
        }
    )
    bha_run: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "BhaRun",
            "type": "Element",
        }
    )
