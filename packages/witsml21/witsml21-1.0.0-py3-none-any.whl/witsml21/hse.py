from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.incident import Incident
from witsml21.pressure_measure import PressureMeasure
from witsml21.time_measure import TimeMeasure
from witsml21.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Hse:
    """Operations Health, Safety and Environment Schema.

    Captures data related to HSE events (e.g., tests, inspections,
    meetings, and drills), test values (e.g., pressure tested to),
    and/or incidents (e.g., discharges, non-compliance notices received,
    etc.).

    :ivar days_inc_free: Incident free duration (commonly in days).
    :ivar last_csg_pres_test: Last casing pressure test date and time.
    :ivar pres_last_csg: Last casing pressure test pressure.
    :ivar last_bop_pres_test: Last blow out preventer pressure test.
    :ivar next_bop_pres_test: Next blow out preventer pressure test.
    :ivar pres_std_pipe: Standpipe manifold pressure tested to.
    :ivar pres_kelly_hose: Kelly hose pressure tested to.
    :ivar pres_diverter: Blow out preventer diverter pressure tested to.
    :ivar pres_annular: Blow out preventer annular preventer pressure
        tested to.
    :ivar pres_rams: Blow out preventer ram pressure tested to.
    :ivar pres_choke_line: Choke line pressure tested to.
    :ivar pres_choke_man: Choke line manifold pressure tested to.
    :ivar last_fire_boat_drill: Last fire or life boat drill.
    :ivar last_abandon_drill: Last abandonment drill.
    :ivar last_rig_inspection: Last rig inspection/check.
    :ivar last_safety_meeting: Last safety meeting.
    :ivar last_safety_inspection: Last safety inspection.
    :ivar last_trip_drill: Last trip drill.
    :ivar last_diverter_drill: Last diverter drill.
    :ivar last_bop_drill: Last blow out preventer drill.
    :ivar reg_agency_insp: Governmental regulatory inspection agency
        inspection? Values are "true" (or "1") and "false" (or "0").
    :ivar non_compliance_issued: Inspection non-compliance notice
        served? Values are "true" (or "1") and "false" (or "0").
    :ivar num_stop_cards: Number of health, safety and environment
        incidents reported.
    :ivar fluid_discharged: Daily whole mud discarded.
    :ivar vol_ctg_discharged: Volume of cuttings discharged.
    :ivar vol_oil_ctg_discharge: Oil on cuttings daily discharge.
    :ivar waste_discharged: Volume of sanitary waste discharged.
    :ivar comments: Comments and remarks.
    :ivar incident:
    """
    days_inc_free: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "DaysIncFree",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    last_csg_pres_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastCsgPresTest",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    pres_last_csg: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresLastCsg",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    last_bop_pres_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastBopPresTest",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    next_bop_pres_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "NextBopPresTest",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    pres_std_pipe: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresStdPipe",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_kelly_hose: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresKellyHose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_diverter: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresDiverter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_annular: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresAnnular",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_rams: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresRams",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_choke_line: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresChokeLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_choke_man: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresChokeMan",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    last_fire_boat_drill: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastFireBoatDrill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    last_abandon_drill: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastAbandonDrill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    last_rig_inspection: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastRigInspection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    last_safety_meeting: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastSafetyMeeting",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    last_safety_inspection: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastSafetyInspection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    last_trip_drill: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastTripDrill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    last_diverter_drill: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastDiverterDrill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    last_bop_drill: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastBopDrill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    reg_agency_insp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RegAgencyInsp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    non_compliance_issued: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonComplianceIssued",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_stop_cards: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumStopCards",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_discharged: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidDischarged",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_ctg_discharged: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolCtgDischarged",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_oil_ctg_discharge: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolOilCtgDischarge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    waste_discharged: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WasteDischarged",
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
    incident: List[Incident] = field(
        default_factory=list,
        metadata={
            "name": "Incident",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
