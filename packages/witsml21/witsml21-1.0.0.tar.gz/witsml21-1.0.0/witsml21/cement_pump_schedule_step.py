from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.component_reference import ComponentReference
from witsml21.pressure_measure import PressureMeasure
from witsml21.time_measure import TimeMeasure
from witsml21.volume_measure import VolumeMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure
from witsml21.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CementPumpScheduleStep:
    """
    Cement Pump Schedule Component Schema, which defines the cement pumping
    schedule for a given step in a cement job.

    :ivar fluid: Reference to a fluid used in CementJob.
    :ivar ratio_fluid_excess: The ratio of excess fluid to total fluid
        pumped during the step.
    :ivar etim_pump: The duration of the fluid pumping.
    :ivar rate_pump: Rate at which the fluid is pumped. 0 means it is a
        pause.
    :ivar vol_pump: Volume pumped = eTimPump * ratePump.
    :ivar stroke_pump: Number of pump strokes for the fluid to be pumped
        (assumes the pump output is known).
    :ivar pres_back: Back pressure applied during the pumping stage.
    :ivar etim_shutdown: The duration of the shutdown event.
    :ivar comments: Comments and remarks.
    :ivar uid: Unique identifier for this pump schedule step.
    """
    fluid: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "Fluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    ratio_fluid_excess: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "RatioFluidExcess",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_pump: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimPump",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rate_pump: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "RatePump",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_pump: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolPump",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stroke_pump: Optional[int] = field(
        default=None,
        metadata={
            "name": "StrokePump",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_back: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresBack",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_shutdown: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimShutdown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
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
