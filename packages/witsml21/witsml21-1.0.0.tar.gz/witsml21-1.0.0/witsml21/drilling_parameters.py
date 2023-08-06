from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.dxc_statistics import DxcStatistics
from witsml21.ecd_statistics import EcdStatistics
from witsml21.mud_density_statistics import MudDensityStatistics
from witsml21.rop_statistics import RopStatistics
from witsml21.rpm_statistics import RpmStatistics
from witsml21.torque_current_statistics import TorqueCurrentStatistics
from witsml21.torque_statistics import TorqueStatistics
from witsml21.wob_statistics import WobStatistics

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillingParameters:
    """
    Information regarding drilling: ROP, WOB, torque, etc.

    :ivar rop: Rate of penetration through the interval.
    :ivar average_weight_on_bit: Surface weight on bit: average through
        the interval.
    :ivar average_torque: Average torque through the interval.
    :ivar average_torque_current: Average torque current through the
        interval. This is the raw measurement from which the average
        torque can be calculated.
    :ivar average_turn_rate: Average turn rate through the interval
        (commonly in rpm).
    :ivar average_mud_density: Average mud density through the interval.
    :ivar average_ecd_at_td: Average effective circulating density at TD
        through the interval.
    :ivar average_drilling_coefficient: Average drilling exponent
        through the interval.
    """
    rop: Optional[RopStatistics] = field(
        default=None,
        metadata={
            "name": "Rop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    average_weight_on_bit: Optional[WobStatistics] = field(
        default=None,
        metadata={
            "name": "AverageWeightOnBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    average_torque: Optional[TorqueStatistics] = field(
        default=None,
        metadata={
            "name": "AverageTorque",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    average_torque_current: Optional[TorqueCurrentStatistics] = field(
        default=None,
        metadata={
            "name": "AverageTorqueCurrent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    average_turn_rate: Optional[RpmStatistics] = field(
        default=None,
        metadata={
            "name": "AverageTurnRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    average_mud_density: Optional[MudDensityStatistics] = field(
        default=None,
        metadata={
            "name": "AverageMudDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    average_ecd_at_td: Optional[EcdStatistics] = field(
        default=None,
        metadata={
            "name": "AverageEcdAtTd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    average_drilling_coefficient: Optional[DxcStatistics] = field(
        default=None,
        metadata={
            "name": "AverageDrillingCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
