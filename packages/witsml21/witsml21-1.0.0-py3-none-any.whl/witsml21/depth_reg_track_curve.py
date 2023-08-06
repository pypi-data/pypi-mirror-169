from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.backup_scale_type import BackupScaleType
from witsml21.depth_reg_rectangle import DepthRegRectangle
from witsml21.line_style import LineStyle
from witsml21.scale_type import ScaleType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthRegTrackCurve:
    """
    Descriptions of the actual curve, including elements such as line weight,
    color, and style, within a log track.

    :ivar curve_info: Curve mnemonic
    :ivar line_style: Image line style
    :ivar line_weight: Description of line graveness
    :ivar line_color: Color of this line
    :ivar curve_scale_type: Scale linearity
    :ivar curve_unit: Unit of data represented
    :ivar curve_left_scale_value: Scale value on the left axis
    :ivar curve_right_scale_value: Scale value on the right axis
    :ivar curve_backup_scale_type: Scale of the backup curve
    :ivar curve_scale_rect: Coordinates of rectangle representing the
        area describing the scale.
    :ivar description: Details of the line
    :ivar uid: Unique identifier for the curve.
    """
    curve_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurveInfo",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    line_style: Optional[LineStyle] = field(
        default=None,
        metadata={
            "name": "LineStyle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    line_weight: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    line_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    curve_scale_type: Optional[ScaleType] = field(
        default=None,
        metadata={
            "name": "CurveScaleType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    curve_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurveUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    curve_left_scale_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "CurveLeftScaleValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    curve_right_scale_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "CurveRightScaleValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    curve_backup_scale_type: Optional[BackupScaleType] = field(
        default=None,
        metadata={
            "name": "CurveBackupScaleType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    curve_scale_rect: List[DepthRegRectangle] = field(
        default_factory=list,
        metadata={
            "name": "CurveScaleRect",
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
