from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.pressure_measure import PressureMeasure
from witsml21.volume_measure import VolumeMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimPumpFlowBackTestStep:
    """
    In a step-down pump diagnostics test, this object contains all the data for
    a particular step in that test.

    :ivar dtim: Time stamp of the pressure measurement.
    :ivar flowback_volume: Volume of flowback since the start of the
        test.
    :ivar flowback_volume_rate: Flowback rate.
    :ivar number: The number of the step. Identifies the step within the
        step down test.
    :ivar bottomhole_rate: Bottomhole flow rate for the specific step.
    :ivar pres: Surface pressure measured for the specific step.
    :ivar pipe_friction: Calculated pipe friction for the specific step.
    :ivar entry_friction: Calculated entry friction accounting for
        perforation and near wellbore restrictions for the specific
        step.
    :ivar perf_friction: Calculated perforation friction for the
        specific step.
    :ivar near_wellbore_friction: Calculated near-wellbore friction
        loss.
    :ivar surface_rate: Surface rate entering the well for the specific
        step.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        StimPumpFlowBackTestStep.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    flowback_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowbackVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowback_volume_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowbackVolumeRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    bottomhole_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "BottomholeRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Pres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pipe_friction: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PipeFriction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    entry_friction: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "EntryFriction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perf_friction: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PerfFriction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    near_wellbore_friction: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "NearWellboreFriction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    surface_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "SurfaceRate",
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
