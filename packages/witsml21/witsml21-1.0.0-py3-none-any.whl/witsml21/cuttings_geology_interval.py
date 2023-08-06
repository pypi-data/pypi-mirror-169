from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_interval_growing_part import AbstractMdIntervalGrowingPart
from witsml21.cuttings_interval_lithology import CuttingsIntervalLithology
from witsml21.dimensionless_measure import DimensionlessMeasure
from witsml21.illuminance_measure import IlluminanceMeasure
from witsml21.length_measure import LengthMeasure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure
from witsml21.time_measure import TimeMeasure
from witsml21.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CuttingsGeologyInterval(AbstractMdIntervalGrowingPart):
    """A depth range along the wellbore containing one or more lithology types
    and information about how the cuttings were sampled.

    These intervals can be sent via ETP using the GrowingObject
    protocol.

    :ivar dens_bulk: Sample bulk density for the interval.
    :ivar dens_shale: Shale density for the interval.
    :ivar calcite: Calcimetry calcite percentage.
    :ivar calc_stab: Calcimetry stabilized percentage.
    :ivar cec: Cuttings cationic exchange capacity. Temporarily calling
        this a DimensionlessMeasure.
    :ivar dolomite: Calcimetry dolomite percentage.
    :ivar size_min: Minimum size.
    :ivar size_max: Maximum size.
    :ivar qft: Fluorescence as measured using a device licensed for the
        Quantitative Fluorescence Technique.
    :ivar cleaning_method: Sample treatment: cleaning method.
    :ivar drying_method: Sample treatment: drying method.
    :ivar bottoms_up_time: Time required for a sample to leave the
        bottomhole and reach the surface.
    :ivar cuttings_interval_lithology:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    dens_bulk: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensBulk",
            "type": "Element",
        }
    )
    dens_shale: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensShale",
            "type": "Element",
        }
    )
    calcite: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Calcite",
            "type": "Element",
        }
    )
    calc_stab: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CalcStab",
            "type": "Element",
        }
    )
    cec: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "Cec",
            "type": "Element",
        }
    )
    dolomite: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Dolomite",
            "type": "Element",
        }
    )
    size_min: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SizeMin",
            "type": "Element",
        }
    )
    size_max: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SizeMax",
            "type": "Element",
        }
    )
    qft: Optional[IlluminanceMeasure] = field(
        default=None,
        metadata={
            "name": "Qft",
            "type": "Element",
        }
    )
    cleaning_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "CleaningMethod",
            "type": "Element",
            "max_length": 64,
        }
    )
    drying_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "DryingMethod",
            "type": "Element",
            "max_length": 64,
        }
    )
    bottoms_up_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "BottomsUpTime",
            "type": "Element",
            "required": True,
        }
    )
    cuttings_interval_lithology: List[CuttingsIntervalLithology] = field(
        default_factory=list,
        metadata={
            "name": "CuttingsIntervalLithology",
            "type": "Element",
        }
    )
