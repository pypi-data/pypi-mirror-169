from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.dimensionless_measure import DimensionlessMeasure
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.force_per_volume_measure import ForcePerVolumeMeasure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure
from witsml21.power_measure import PowerMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.stim_fluid import StimFluid
from witsml21.stim_material_quantity import StimMaterialQuantity
from witsml21.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml21.time_measure import TimeMeasure
from witsml21.volume_measure import VolumeMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure
from witsml21.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimJobStep:
    """
    A step in the treatment of a stage for a stimulation job.

    :ivar step_name: A human readable name for the step.
    :ivar step_number: Step number.
    :ivar kind: The type of step.
    :ivar description: A short description of the step.
    :ivar dtim_start: Date and time the step started.
    :ivar dtim_end: Date and time the step ended.
    :ivar avg_base_fluid_quality: Base quality percentage of foam.
    :ivar avg_co2_base_fluid_quality: Base quality carbon dioxide
        percent of foam.
    :ivar avg_hydraulic_power: Average hydraulic horse power used.
    :ivar avg_internal_phase_fraction: Internal gas phase percentage of
        the foam.
    :ivar avg_material_used_rate: Average material used per minute
        entering the flow stream.
    :ivar avg_material_use_rate_bottomhole: Average material amount used
        (pumped) per minute at bottomhole.
    :ivar avg_n2_base_fluid_quality: Base quality nitrogen percentage of
        foam.
    :ivar avg_pres_bottomhole: Average bottomhole pressure.
    :ivar avg_pres_surface: Average surface pressure.
    :ivar avg_prop_conc: Average proppant concentration at the wellhead.
        ppa: pounds proppant added per volume measure kgpa: kilograms
        proppant added per volume measure
    :ivar avg_proppant_conc_bottomhole: The average proppant
        concentration at bottomhole.
    :ivar avg_proppant_conc_surface: The average proppant concentration
        at the surface.
    :ivar avg_slurry_prop_conc: Average proppant concentration exiting
        the equipment.
    :ivar avg_slurry_rate: Average slurry return rate.
    :ivar avg_temperature: Average fluid temperature.
    :ivar avg_volume_rate_wellhead: Average volume per minute at the
        wellhead.
    :ivar balls_recovered: Balls recovered during execution of the step.
    :ivar balls_used: Balls used during execution of the step.
    :ivar base_fluid_bypass_vol: Base fluid volume recorded after
        equipment set to bypass.
    :ivar base_fluid_vol: Base fluid volume entering the equipment.
    :ivar end_dirty_material_rate: Ending dirty fluid pump volume per
        minute.
    :ivar end_material_used_rate: Ending quantity of material used per
        minute entering the flow stream.
    :ivar end_material_used_rate_bottomhole: Ending quantity of material
        used per minute at bottomhole.
    :ivar end_pres_bottomhole: Final bottomhole pressure.
    :ivar end_pres_surface: Final surface pressure.
    :ivar end_proppant_conc_bottomhole: The final proppant concentration
        at bottomhole.
    :ivar end_proppant_conc_surface: The final proppant concentration at
        the surface.
    :ivar end_rate_surface_co2: Final CO2 pump rate in volume per time
        at the surface.
    :ivar end_std_rate_surface_n2: Final nitrogen pump rate in volume
        per time at the surface.
    :ivar fluid_vol_base: The step volume of the base step.
    :ivar fluid_vol_circulated: Fluid volume circulated.
    :ivar fluid_vol_pumped: Fluid volume pumped.
    :ivar fluid_vol_returned: Fluid volume returned.
    :ivar fluid_vol_slurry: The volume of the slurry (dirty) step.
    :ivar fluid_vol_squeezed: Fluid volume squeezed.
    :ivar fluid_vol_washed: Fluid volume washed.
    :ivar fracture_gradient_final: The fracture gradient when the step
        ends.
    :ivar fracture_gradient_initial: The fracture gradient before
        starting the step.
    :ivar friction_factor: Numeric value used to scale a calculated
        rheological friction.
    :ivar max_hydraulic_power: Maximum hydraulic power used during the
        step.
    :ivar max_pres_surface: Maximum pumping pressure on surface.
    :ivar max_proppant_conc_bottomhole: Maximum proppant concentration
        at bottomhole during the stimulation step.
    :ivar max_proppant_conc_surface: Maximum proppant concentration at
        the wellhead.
    :ivar max_slurry_prop_conc: Maximum proppant concentration exiting
        the equipment.
    :ivar max_volume_rate_wellhead: Maximum volume per minute at the
        wellhead.
    :ivar pipe_friction_pressure: The friction pressure contribution
        from pipes.
    :ivar pump_time: Total pumping time for the step.
    :ivar start_dirty_material_rate: Starting dirty fluid volume per
        minute.
    :ivar start_material_used_rate: Starting quantity of material used
        per minute entering the flow stream.
    :ivar start_material_used_rate_bottom_hole: Starting quantity of
        material used per minute at bottomhole.
    :ivar start_pres_bottomhole: Starting bottomhole pressure.
    :ivar start_pres_surface: Starting surface pressure.
    :ivar start_proppant_conc_bottomhole: The beginning proppant
        concentration at bottomhole.
    :ivar start_proppant_conc_surface: The beginning proppant
        concentration at the surface.
    :ivar wellhead_vol: Slurry volume entering the well.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar material_used: Material used during the step
    :ivar max_material_used_rate:
    :ivar fluid:
    :ivar uid: Unique identifier for this instance of StimJobStep.
    """
    step_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "StepName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    step_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "StepNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    avg_base_fluid_quality: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgBaseFluidQuality",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_co2_base_fluid_quality: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgCO2BaseFluidQuality",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_hydraulic_power: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "AvgHydraulicPower",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_internal_phase_fraction: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgInternalPhaseFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_material_used_rate: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "AvgMaterialUsedRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_material_use_rate_bottomhole: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "AvgMaterialUseRateBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_n2_base_fluid_quality: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgN2BaseFluidQuality",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_pres_bottomhole: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgPresBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_pres_surface: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgPresSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_prop_conc: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgPropConc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_proppant_conc_bottomhole: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgProppantConcBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_proppant_conc_surface: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgProppantConcSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_slurry_prop_conc: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgSlurryPropConc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_slurry_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgSlurryRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_volume_rate_wellhead: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgVolumeRateWellhead",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    balls_recovered: Optional[int] = field(
        default=None,
        metadata={
            "name": "BallsRecovered",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_inclusive": 0,
        }
    )
    balls_used: Optional[int] = field(
        default=None,
        metadata={
            "name": "BallsUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_inclusive": 0,
        }
    )
    base_fluid_bypass_vol: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BaseFluidBypassVol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    base_fluid_vol: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BaseFluidVol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_dirty_material_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "EndDirtyMaterialRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_material_used_rate: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "EndMaterialUsedRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_material_used_rate_bottomhole: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "EndMaterialUsedRateBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_pres_bottomhole: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "EndPresBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_pres_surface: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "EndPresSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_proppant_conc_bottomhole: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "EndProppantConcBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_proppant_conc_surface: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "EndProppantConcSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_rate_surface_co2: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "EndRateSurfaceCO2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_std_rate_surface_n2: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "EndStdRateSurfaceN2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_vol_base: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidVolBase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_vol_circulated: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidVolCirculated",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_vol_pumped: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidVolPumped",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_vol_returned: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidVolReturned",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_vol_slurry: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidVolSlurry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_vol_squeezed: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidVolSqueezed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_vol_washed: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidVolWashed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fracture_gradient_final: Optional[ForcePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FractureGradientFinal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fracture_gradient_initial: Optional[ForcePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FractureGradientInitial",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    friction_factor: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "FrictionFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_hydraulic_power: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "MaxHydraulicPower",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_pres_surface: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "MaxPresSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_proppant_conc_bottomhole: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxProppantConcBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_proppant_conc_surface: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxProppantConcSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_slurry_prop_conc: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxSlurryPropConc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_volume_rate_wellhead: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxVolumeRateWellhead",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pipe_friction_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PipeFrictionPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pump_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "PumpTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start_dirty_material_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "StartDirtyMaterialRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start_material_used_rate: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "StartMaterialUsedRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start_material_used_rate_bottom_hole: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "StartMaterialUsedRateBottomHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start_pres_bottomhole: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "StartPresBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start_pres_surface: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "StartPresSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start_proppant_conc_bottomhole: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "StartProppantConcBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start_proppant_conc_surface: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "StartProppantConcSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wellhead_vol: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WellheadVol",
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
    material_used: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "MaterialUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_material_used_rate: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "MaxMaterialUsedRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid: Optional[StimFluid] = field(
        default=None,
        metadata={
            "name": "Fluid",
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
