from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.pressure_measure import PressureMeasure
from witsml21.stim_pump_flow_back_test_step import StimPumpFlowBackTestStep
from witsml21.time_measure import TimeMeasure
from witsml21.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimPumpFlowBackTest:
    """
    Diagnostic test involving flowing a well back after treatment.

    :ivar dtim_end: End time for the test.
    :ivar flow_back_volume: Total volume recovered during a flow back
        test.
    :ivar dtim_start: Start time for the test.
    :ivar fracture_close_duration: The time required for the fracture
        width to become zero.
    :ivar pres_casing: Casing pressure.
    :ivar pres_tubing: Tubing pressure.
    :ivar fracture_close_pres: The pressure when the fracture width
        becomes zero.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar step:
    :ivar uid: Unique identifier for this instance of
        StimPumpFlowBackTest.
    """
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    flow_back_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowBackVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    fracture_close_duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "FractureCloseDuration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_casing: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresCasing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_tubing: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresTubing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fracture_close_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FractureClosePres",
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
    step: List[StimPumpFlowBackTestStep] = field(
        default_factory=list,
        metadata={
            "name": "Step",
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
