from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_object import AbstractObject
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.length_measure import LengthMeasure
from witsml21.md_interval import MdInterval
from witsml21.plane_angle_measure import PlaneAngleMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.reciprocal_length_measure import ReciprocalLengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimPerforationCluster(AbstractObject):
    """Information about a set of perforations.

    The assumption is that all perforations within a given set are
    created with the same device or method.

    :ivar md_perforated_interval: Measured depths of the top and base
        perforation.
    :ivar tvd_perforated_interval: True vertical depth of the top and
        base perforation.
    :ivar type: The type of perforation and/or how the perforation was
        created.
    :ivar perforation_count: The number of perforations in this
        interval.
    :ivar size: The size of the perforations.
    :ivar density_perforation: The number of perforation holes per
        length across the treatment interval. Used to describe but not
        limited to the configuration of perforating guns or the
        placement of perforations (holes, slots, openings, etc.) in the
        wellbore, and is often abbreviated to spf (shots per foot).
    :ivar phasing_perforation: The radial distribution of successive
        perforations around the wellbore axis. Radial distribution is
        commonly available in 0, 180 120, 90 and 60 degree phasing.
    :ivar friction_factor: The friction factor of each perforation set.
    :ivar friction_pres: The friction pressure for the perforation set.
    :ivar discharge_coefficient: A coefficient used in the equation for
        calculation of pressure drop across a perforation set.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    md_perforated_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdPerforatedInterval",
            "type": "Element",
        }
    )
    tvd_perforated_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "TvdPerforatedInterval",
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "max_length": 64,
        }
    )
    perforation_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PerforationCount",
            "type": "Element",
            "min_inclusive": 0,
        }
    )
    size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Element",
        }
    )
    density_perforation: Optional[ReciprocalLengthMeasure] = field(
        default=None,
        metadata={
            "name": "DensityPerforation",
            "type": "Element",
        }
    )
    phasing_perforation: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "PhasingPerforation",
            "type": "Element",
        }
    )
    friction_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "FrictionFactor",
            "type": "Element",
        }
    )
    friction_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FrictionPres",
            "type": "Element",
        }
    )
    discharge_coefficient: Optional[float] = field(
        default=None,
        metadata={
            "name": "DischargeCoefficient",
            "type": "Element",
        }
    )
