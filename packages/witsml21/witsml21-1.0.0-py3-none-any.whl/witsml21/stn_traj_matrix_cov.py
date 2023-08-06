from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.area_measure import AreaMeasure
from witsml21.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StnTrajMatrixCov:
    """
    Captures validation information for a covariance matrix.

    :ivar variance_nn: Covariance north north.
    :ivar variance_ne: Crossvariance north east.
    :ivar variance_nvert: Crossvariance north vertical.
    :ivar variance_ee: Covariance east east.
    :ivar variance_evert: Crossvariance east vertical.
    :ivar variance_vert_vert: Covariance vertical vertical.
    :ivar bias_n: Bias north.
    :ivar bias_e: Bias east.
    :ivar bias_vert: Bias vertical. The coordinate system is set up in a
        right-handed configuration, which makes the vertical direction
        increasing (i.e., positive) downwards.
    :ivar sigma: The sigma which is appropriate for all the other values
        in this class.
    """
    variance_nn: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceNN",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    variance_ne: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceNE",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    variance_nvert: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceNVert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    variance_ee: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceEE",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    variance_evert: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceEVert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    variance_vert_vert: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceVertVert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    bias_n: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BiasN",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    bias_e: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BiasE",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    bias_vert: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BiasVert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    sigma: Optional[float] = field(
        default=None,
        metadata={
            "name": "Sigma",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
