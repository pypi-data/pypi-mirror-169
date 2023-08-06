from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_object import AbstractObject
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.data_object_reference import DataObjectReference
from witsml21.force_per_volume_measure import ForcePerVolumeMeasure
from witsml21.length_measure import LengthMeasure
from witsml21.length_per_time_measure import LengthPerTimeMeasure
from witsml21.mass_measure import MassMeasure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure
from witsml21.measured_depth import MeasuredDepth
from witsml21.power_measure import PowerMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.pressure_measure_ext import PressureMeasureExt
from witsml21.stim_event import StimEvent
from witsml21.stim_flow_path import StimFlowPath
from witsml21.stim_job_diagnostic_session import StimJobDiagnosticSession
from witsml21.stim_job_diversion import StimJobDiversion
from witsml21.stim_job_step import StimJobStep
from witsml21.stim_material_quantity import StimMaterialQuantity
from witsml21.stim_perforation_cluster_set import StimPerforationClusterSet
from witsml21.stim_reservoir_interval import StimReservoirInterval
from witsml21.stim_shut_in_pressure import StimShutInPressure
from witsml21.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml21.time_measure import TimeMeasure
from witsml21.volume_measure import VolumeMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure
from witsml21.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimJobStage(AbstractObject):
    """
    Stage treated during a stimulation job.

    :ivar number: The number associated with the stage.
    :ivar fracture_height: The height of the fracture.
    :ivar percent_pad: The percentage of volume pumped used for the pad.
    :ivar stage_perforation_clusters: Perforations added just before
        treating the stage.
    :ivar avg_base_fluid_return_volume_rate: Average base fluid pumping
        rate of all steps for stage treatment.
    :ivar avg_bhstatic_temperature: The average static temperature of
        the wellbore injection point(s) or formation at equilibrium
        (steady state) with no fluid or tool movement, allowing for
        equilibrium conditions at the wellbore injection point; (BHST:
        bottom hole static temperature.
    :ivar avg_bhtreating_temperature: The average measured or calculated
        temperature of the wellbore during the treating with well fluid
        injection or circulation of the wellbore at the point of
        interest. Point of interest is generally the injection point or
        region of interest for the test or treatment.
    :ivar avg_bottomhole_pumped_volume_rate: Average bottomhole
        treatment flow rate.
    :ivar avg_conductivity: Average conductivity of a fracture created
        during the treatment supported by proppant during the
        stimulation services Hydraulic conductivity, symbolically
        represented as K, is a property of vascular plants, soil or
        rock, that describes the ease with which water can move through
        pore spaces or fractures. It depends on the intrinsic
        permeability of the material and on the degree of saturation.
        Saturated hydraulic conductivity, Ksat, describes water movement
        through saturated media.
    :ivar avg_fracture_width: Average fracture width created during the
        treatment of the stage.
    :ivar avg_hydraulic_power: Average hydraulic horse power used.
    :ivar avg_pres_annulus: The average annulus pressure for any step
        for the stage treatment.
    :ivar avg_pres_casing: The average casing pressure of any step for
        the stage treatment.
    :ivar avg_pres_surface: The average pressure for treating the stage
        across all steps.
    :ivar avg_pres_tubing: The average tubing pressure of any step for
        the stage treatment.
    :ivar avg_proppant_conc_bottomhole: The average proppant
        concentration at the bottom of the hole.
    :ivar avg_proppant_conc_surface: The average proppant concentration
        on the surface.
    :ivar avg_slurry_return_volume_rate: The average slurry return rate
        of all steps for the stage treatment.
    :ivar break_down_pres: The pressure at which the formation fractures
        and accepts injected fluid.
    :ivar closure_duration: Delta time recorded for the closure of the
        fracture to occur during the stage treatment.
    :ivar closure_pres: An analysis parameter used in hydraulic fracture
        design to indicate the pressure at which the fracture
        effectively closes without proppant in place.
    :ivar dtim_end: Ending date and time for the stage treatment.
    :ivar dtim_start: Starting date and time for the stage treatment.
    :ivar formation_break_length_per_day: The length of formation broken
        per day.
    :ivar formation_name: The name of the formation being stimulated.
    :ivar formation_proppant_mass: The weight of proppant placed in the
        formation.
    :ivar fracture_gradient_final: The formation fracture gradient for
        the stage after treatment.
    :ivar fracture_gradient_initial: The formation fracture gradient for
        stage before treatment.
    :ivar fracture_length: The length of the fracture created after
        treating the stage.
    :ivar friction_pressure: Friction pressure loss.
    :ivar hhp_ordered_co2: Carbon dioxide hydraulic horsepower ordered
        for the stage.
    :ivar hhp_ordered_fluid: Fluid hydraulic horsepower ordered for the
        stage.
    :ivar hhp_used_co2: Carbon dioxide hydraulic horsepower actually
        used for the stage.
    :ivar hhp_used_fluid: Fluid hydraulic horsepower actually used for
        the stage.
    :ivar initial_shutin_pres: The initial shut-in pressure.
    :ivar max_fluid_volume_rate_annulus: Maximum annulus fluid pumping
        rate of any step while treating the stage.
    :ivar max_fluid_volume_rate_casing: Maximum casing fluid pumping
        rate of any step while treating the stage.
    :ivar max_fluid_volume_rate_tubing: Maximum tubing fluid pumping
        rate of any step while treating the stage.
    :ivar max_hydraulic_power: Maximum hydraulic horse power used for
        the stage.
    :ivar max_pres_annulus: The highest annulus pressure of any step
        while treating the stage.
    :ivar max_pres_casing: The highest casing pressure of any step while
        treating the stage.
    :ivar max_pres_surface: Maximum surface pressure during treatment of
        the stage.
    :ivar max_pres_tubing: The highest tubing pressure of any step while
        treating the stage.
    :ivar max_proppant_conc_bottomhole: The maximum proppant
        concentration at the bottom of the wellbore.
    :ivar max_proppant_conc_surface: The maximum proppant concentration
        on the surface.
    :ivar md_formation_bottom: Measured depth of the bottom of the
        formation.
    :ivar md_formation_top: Measured depth of the top of the formation.
    :ivar md_open_hole_bottom: Measured depth of the bottom open hole.
    :ivar md_open_hole_top: Measured depth of the top open hole.
    :ivar net_pres: The difference between the pressure which holds a
        fracture closed (minimal principal stress) and that pressure
        which is necessary to open the fracture.
    :ivar open_hole_diameter: The diameter of the open hole.
    :ivar open_hole_name: A name for the open hole. To be used for open
        hole completions.
    :ivar percent_proppant_pumped: Total proppant mass used as a percent
        of the design mass.
    :ivar perf_ball_count: Total number of perforation balls used while
        treating the stage.
    :ivar perf_ball_size: The size of the perforation balls used while
        treating the stage
    :ivar perf_proppant_conc: The proppant concentration at the
        perforations.
    :ivar proppant_height: The proppant height.
    :ivar screened_out: Did screen out occur? True ("true" or "1")
        indicates that screen out occurred. False ("false" or "0") or
        not given indicates otherwise.
    :ivar screen_out_pres: The screen out pressure.
    :ivar technology_type: Text describing the technology used while
        pumping the stage.
    :ivar total_proppant_in_formation: The total amount of proppant in
        the formation relative to the current stage.
    :ivar total_pump_time: The total pumping time for the treatment of
        the stage.
    :ivar total_volume: The total volume pumped for all steps while
        treating the stage.
    :ivar tvd_formation_bottom: True vertical depth of the bottom of the
        formation.
    :ivar tvd_formation_top: True vertical depth of the top of the
        formation.
    :ivar tvd_open_hole_bottom: True vertical depth of the bottom open
        hole.
    :ivar tvd_open_hole_top: True vertical depth of the top open hole.
    :ivar volume_body: The volume pumped for the body portion of the
        stage treatment.
    :ivar volume_flush: Volume pumped during flush portion of stage
        treatment.
    :ivar volume_pad: Volume pumped for pad portion of stage treatment.
    :ivar water_source: Water source for fluid pumped during stage.
    :ivar wellbore_proppant_mass: The weight of proppant left in the
        wellbore after pumping has stopped.
    :ivar pdat_session:
    :ivar shut_in_pres:
    :ivar job_event:
    :ivar job_step:
    :ivar max_material_usage_rate:
    :ivar material_used:
    :ivar flow_path:
    :ivar reservoir_interval:
    :ivar stim_stage_log:
    :ivar diversion:
    :ivar uid: Unique identifier for this instance of StimJobStage.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "min_inclusive": 1,
        }
    )
    fracture_height: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FractureHeight",
            "type": "Element",
        }
    )
    percent_pad: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PercentPad",
            "type": "Element",
        }
    )
    stage_perforation_clusters: Optional[StimPerforationClusterSet] = field(
        default=None,
        metadata={
            "name": "StagePerforationClusters",
            "type": "Element",
        }
    )
    avg_base_fluid_return_volume_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgBaseFluidReturnVolumeRate",
            "type": "Element",
        }
    )
    avg_bhstatic_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgBHStaticTemperature",
            "type": "Element",
        }
    )
    avg_bhtreating_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgBHTreatingTemperature",
            "type": "Element",
        }
    )
    avg_bottomhole_pumped_volume_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgBottomholePumpedVolumeRate",
            "type": "Element",
        }
    )
    avg_conductivity: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgConductivity",
            "type": "Element",
        }
    )
    avg_fracture_width: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "AvgFractureWidth",
            "type": "Element",
        }
    )
    avg_hydraulic_power: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "AvgHydraulicPower",
            "type": "Element",
        }
    )
    avg_pres_annulus: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgPresAnnulus",
            "type": "Element",
        }
    )
    avg_pres_casing: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgPresCasing",
            "type": "Element",
        }
    )
    avg_pres_surface: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgPresSurface",
            "type": "Element",
        }
    )
    avg_pres_tubing: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgPresTubing",
            "type": "Element",
        }
    )
    avg_proppant_conc_bottomhole: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgProppantConcBottomhole",
            "type": "Element",
        }
    )
    avg_proppant_conc_surface: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgProppantConcSurface",
            "type": "Element",
        }
    )
    avg_slurry_return_volume_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgSlurryReturnVolumeRate",
            "type": "Element",
        }
    )
    break_down_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "BreakDownPres",
            "type": "Element",
        }
    )
    closure_duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ClosureDuration",
            "type": "Element",
        }
    )
    closure_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "ClosurePres",
            "type": "Element",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    formation_break_length_per_day: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FormationBreakLengthPerDay",
            "type": "Element",
        }
    )
    formation_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FormationName",
            "type": "Element",
            "max_length": 2000,
        }
    )
    formation_proppant_mass: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "FormationProppantMass",
            "type": "Element",
        }
    )
    fracture_gradient_final: Optional[ForcePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FractureGradientFinal",
            "type": "Element",
        }
    )
    fracture_gradient_initial: Optional[ForcePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FractureGradientInitial",
            "type": "Element",
        }
    )
    fracture_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FractureLength",
            "type": "Element",
        }
    )
    friction_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FrictionPressure",
            "type": "Element",
        }
    )
    hhp_ordered_co2: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "HhpOrderedCO2",
            "type": "Element",
        }
    )
    hhp_ordered_fluid: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "HhpOrderedFluid",
            "type": "Element",
        }
    )
    hhp_used_co2: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "HhpUsedCO2",
            "type": "Element",
        }
    )
    hhp_used_fluid: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "HhpUsedFluid",
            "type": "Element",
        }
    )
    initial_shutin_pres: Optional[PressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "InitialShutinPres",
            "type": "Element",
        }
    )
    max_fluid_volume_rate_annulus: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxFluidVolumeRateAnnulus",
            "type": "Element",
        }
    )
    max_fluid_volume_rate_casing: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxFluidVolumeRateCasing",
            "type": "Element",
        }
    )
    max_fluid_volume_rate_tubing: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxFluidVolumeRateTubing",
            "type": "Element",
        }
    )
    max_hydraulic_power: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "MaxHydraulicPower",
            "type": "Element",
        }
    )
    max_pres_annulus: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "MaxPresAnnulus",
            "type": "Element",
        }
    )
    max_pres_casing: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "MaxPresCasing",
            "type": "Element",
        }
    )
    max_pres_surface: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "MaxPresSurface",
            "type": "Element",
        }
    )
    max_pres_tubing: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "MaxPresTubing",
            "type": "Element",
        }
    )
    max_proppant_conc_bottomhole: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxProppantConcBottomhole",
            "type": "Element",
        }
    )
    max_proppant_conc_surface: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxProppantConcSurface",
            "type": "Element",
        }
    )
    md_formation_bottom: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdFormationBottom",
            "type": "Element",
        }
    )
    md_formation_top: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdFormationTop",
            "type": "Element",
        }
    )
    md_open_hole_bottom: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdOpenHoleBottom",
            "type": "Element",
        }
    )
    md_open_hole_top: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdOpenHoleTop",
            "type": "Element",
        }
    )
    net_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "NetPres",
            "type": "Element",
        }
    )
    open_hole_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OpenHoleDiameter",
            "type": "Element",
        }
    )
    open_hole_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OpenHoleName",
            "type": "Element",
            "max_length": 2000,
        }
    )
    percent_proppant_pumped: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PercentProppantPumped",
            "type": "Element",
        }
    )
    perf_ball_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PerfBallCount",
            "type": "Element",
            "min_inclusive": 0,
        }
    )
    perf_ball_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PerfBallSize",
            "type": "Element",
        }
    )
    perf_proppant_conc: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PerfProppantConc",
            "type": "Element",
        }
    )
    proppant_height: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ProppantHeight",
            "type": "Element",
        }
    )
    screened_out: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ScreenedOut",
            "type": "Element",
        }
    )
    screen_out_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "ScreenOutPres",
            "type": "Element",
        }
    )
    technology_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechnologyType",
            "type": "Element",
            "max_length": 64,
        }
    )
    total_proppant_in_formation: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalProppantInFormation",
            "type": "Element",
        }
    )
    total_pump_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "TotalPumpTime",
            "type": "Element",
        }
    )
    total_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "TotalVolume",
            "type": "Element",
        }
    )
    tvd_formation_bottom: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdFormationBottom",
            "type": "Element",
        }
    )
    tvd_formation_top: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdFormationTop",
            "type": "Element",
        }
    )
    tvd_open_hole_bottom: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdOpenHoleBottom",
            "type": "Element",
        }
    )
    tvd_open_hole_top: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdOpenHoleTop",
            "type": "Element",
        }
    )
    volume_body: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeBody",
            "type": "Element",
        }
    )
    volume_flush: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeFlush",
            "type": "Element",
        }
    )
    volume_pad: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumePad",
            "type": "Element",
        }
    )
    water_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "WaterSource",
            "type": "Element",
            "max_length": 2000,
        }
    )
    wellbore_proppant_mass: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "WellboreProppantMass",
            "type": "Element",
        }
    )
    pdat_session: List[StimJobDiagnosticSession] = field(
        default_factory=list,
        metadata={
            "name": "PdatSession",
            "type": "Element",
        }
    )
    shut_in_pres: List[StimShutInPressure] = field(
        default_factory=list,
        metadata={
            "name": "ShutInPres",
            "type": "Element",
        }
    )
    job_event: List[StimEvent] = field(
        default_factory=list,
        metadata={
            "name": "JobEvent",
            "type": "Element",
        }
    )
    job_step: List[StimJobStep] = field(
        default_factory=list,
        metadata={
            "name": "JobStep",
            "type": "Element",
        }
    )
    max_material_usage_rate: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "MaxMaterialUsageRate",
            "type": "Element",
        }
    )
    material_used: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "MaterialUsed",
            "type": "Element",
        }
    )
    flow_path: Optional[StimFlowPath] = field(
        default=None,
        metadata={
            "name": "FlowPath",
            "type": "Element",
        }
    )
    reservoir_interval: List[StimReservoirInterval] = field(
        default_factory=list,
        metadata={
            "name": "ReservoirInterval",
            "type": "Element",
        }
    )
    stim_stage_log: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "StimStageLog",
            "type": "Element",
        }
    )
    diversion: Optional[StimJobDiversion] = field(
        default=None,
        metadata={
            "name": "Diversion",
            "type": "Element",
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
