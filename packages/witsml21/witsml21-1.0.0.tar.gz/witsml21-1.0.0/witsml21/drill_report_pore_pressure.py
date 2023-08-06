from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure
from witsml21.measured_depth import MeasuredDepth
from witsml21.reading_kind import ReadingKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportPorePressure:
    """
    General information about pore pressure related to the drill report period.

    :ivar reading_kind: Indicate if the reading was estimated or
        measured.
    :ivar equivalent_mud_weight: The equivalent mud weight value of the
        pore pressure reading.
    :ivar dtim: Date and time at the reading was recorded.
    :ivar md: Measured depth where the readings were recorded.
    :ivar tvd: True vertical depth where the readings were recorded.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        DrillReportPorePressure.
    """
    reading_kind: Optional[ReadingKind] = field(
        default=None,
        metadata={
            "name": "ReadingKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    equivalent_mud_weight: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "EquivalentMudWeight",
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
    md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "Tvd",
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
