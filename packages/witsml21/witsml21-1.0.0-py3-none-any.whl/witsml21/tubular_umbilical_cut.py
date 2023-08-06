from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.measured_depth import MeasuredDepth

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TubularUmbilicalCut:
    """
    Information about a cut in a TubularUmbilical.

    :ivar cut_date: The date the cut happened.
    :ivar cut_md: Measured Depth at which the cut has happened.
    :ivar is_accidental: Flag indicating whether the cut is accidental
        or not.
    """
    cut_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CutDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    cut_md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "CutMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    is_accidental: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAccidental",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
