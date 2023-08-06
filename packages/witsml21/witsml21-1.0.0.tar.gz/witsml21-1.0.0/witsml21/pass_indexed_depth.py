from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.length_measure_ext import LengthMeasureExt
from witsml21.pass_direction import PassDirection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PassIndexedDepth:
    """
    Qualifies measured depth based on pass, direction and depth.

    :ivar pass_value: The pass number. When pass indexed depth values
        are used as primary index values, the pass number MUST change
        any time direction changes. When used as secondary index values,
        this is not required.
    :ivar direction: The direction of the tool in a pass. For primary
        index values, index values within a pass MUST be strictly
        ordered according to the direction. Holding steady MUST NOT be
        used for primary index values; it is only allowed for secondary
        index values.
    :ivar measured_depth: The measured depth of the point.
    """
    pass_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    direction: Optional[PassDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    measured_depth: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "MeasuredDepth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
