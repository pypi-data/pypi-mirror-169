from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.lithology_qualifier_kind import LithologyQualifierKind
from witsml21.md_interval import MdInterval
from witsml21.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class LithologyQualifier:
    """
    A description of minerals or accessories that constitute a fractional part
    of a CuttingsIntervalLithology.

    :ivar kind: The type of qualifier.
    :ivar md_interval: The measured depth interval represented by the
        qualifier. This must be within the range of the parent geologic
        interval. If MdInterval is not given then the qualifier is
        deemed to exist over the entire depth range of the parent
        geologyInterval.
    :ivar abundance: The relative abundance of the qualifier estimated
        based on a "visual area" by inspecting the cuttings spread out
        on the shaker table before washing, or in the sample tray after
        washing. This represents the upper bound of the observed range,
        and is in the following increments at the upper bound: 1 = less
        than or equal to 1% 2 = greater than 1% and less than 2% 5 =
        greater than or equal to 2% and less than 5% and then in 5%
        increments, 10 (=5-10%), 15 (=10-15%) up to 100 (=95-100%). The
        end user can then elect to either display the %, or map them to
        an operator-specific term or coding, e.g., 1 less than or equal
        to 1% = rare trace, or occasional, or very sparse, etc.,
        depending on the end users' terminology. i.e. 1 less then or
        equal to 1%=Rare Trace, or occasional, or very sparse etc.,
        depending on the the end users' terminology.)
    :ivar description: A textual description of the qualifier.
    :ivar uid: Unique identifier for this instance of LithologyQualifier
    """
    kind: Optional[Union[LithologyQualifierKind, str]] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    abundance: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Abundance",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
