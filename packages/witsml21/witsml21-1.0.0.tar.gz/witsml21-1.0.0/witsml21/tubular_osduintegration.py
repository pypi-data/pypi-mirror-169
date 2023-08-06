from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_measure import LengthMeasure
from witsml21.measured_depth import MeasuredDepth
from witsml21.osdutubular_assembly_status import OsdutubularAssemblyStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TubularOsduintegration:
    """
    Information about a Tubular that is relevant for OSDU integration but does
    not have a natural place in a Tubular object.

    :ivar active_indicator: Indicates if the Assembly is activated or
        not.
    :ivar activity_type: Used to describe if it belongs to a RunActivity
        or to a PullActivity.
    :ivar activity_type_reason_description: Used to describe the reason
        of Activity - such as cut/pull, pulling, ...
    :ivar artificial_lift_type: Type of Artificial Lift used (could be
        "Surface Pump" / "Submersible Pump" / "Gas Lift" ...)
    :ivar assembly_base_md: The measured depth of the base from the
        whole assembly.
    :ivar assembly_base_reported_tvd: Depth of the base of the Assembly
        measured from the Well-Head.
    :ivar assembly_top_md: The measured depth of the top from the whole
        assembly.
    :ivar assembly_top_reported_tvd: Depth of the top of the Assembly
        measured from the Well-Head.
    :ivar liner_type: This reference table describes the type of liner
        used in the borehole. For example, slotted, gravel packed or
        pre-perforated etc.
    :ivar osdutubular_assembly_status: Record that reflects the status
        of the Assembly - as 'installed', 'pulled', 'planned',... -
        Applicable to tubing/completions as opposed to drillstrings.
    :ivar parent: Optional - Identifier of the parent assembly (in case
        of side-track, multi-nesting, ...) - The Concentric Tubular
        model is used to identify the Assembly that an Assembly sits
        inside e.g. Surface Casing set inside Conductor, Tubing set
        inside Production Casing, a Bumper Spring set inside a
        Production Tubing Profile Nipple, Liner set inside Casing, etc.
        This is needed to enable a Digital Well Sketch application to
        understand relationships between Assemblies and their parent
        Wellbores.
    :ivar pilot_hole_size: Diameter of the Pilot Hole.
    :ivar sea_floor_penetration_length: The distance that the assembly
        has penetrated below the surface of the sea floor.
    :ivar string_class: Descriptor for Assembly, e.g. Production,
        Surface, Conductor, Intermediate, Drilling.
    :ivar suspension_point_md: In case of multi-nesting of assemblies,
        the 'point' is the Measured Depth of the top of the assembly
        though with PBRs the Suspension Point may not be the top.
    :ivar tubular_assembly_number: Sequence of the TubularAssembly
        (Typically BHA sequence).
    """
    class Meta:
        name = "TubularOSDUIntegration"

    active_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActiveIndicator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    activity_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActivityType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    activity_type_reason_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActivityTypeReasonDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    artificial_lift_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArtificialLiftType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    assembly_base_md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "AssemblyBaseMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    assembly_base_reported_tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "AssemblyBaseReportedTvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    assembly_top_md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "AssemblyTopMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    assembly_top_reported_tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "AssemblyTopReportedTvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    liner_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinerType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    osdutubular_assembly_status: Optional[OsdutubularAssemblyStatus] = field(
        default=None,
        metadata={
            "name": "OSDUTubularAssemblyStatus",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    parent: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pilot_hole_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PilotHoleSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sea_floor_penetration_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SeaFloorPenetrationLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    string_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "StringClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    suspension_point_md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "SuspensionPointMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular_assembly_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "TubularAssemblyNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
