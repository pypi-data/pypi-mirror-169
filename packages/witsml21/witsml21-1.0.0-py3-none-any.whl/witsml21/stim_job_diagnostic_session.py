from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.dimensionless_measure import DimensionlessMeasure
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.isothermal_compressibility_measure import IsothermalCompressibilityMeasure
from witsml21.length_measure import LengthMeasure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure
from witsml21.measured_depth import MeasuredDepth
from witsml21.pressure_measure import PressureMeasure
from witsml21.specific_heat_capacity_measure import SpecificHeatCapacityMeasure
from witsml21.stim_fet_test import StimFetTest
from witsml21.stim_pump_flow_back_test import StimPumpFlowBackTest
from witsml21.stim_step_down_test import StimStepDownTest
from witsml21.stim_step_test import StimStepTest
from witsml21.thermal_conductivity_measure import ThermalConductivityMeasure
from witsml21.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml21.time_measure import TimeMeasure
from witsml21.volume_measure import VolumeMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure
from witsml21.volume_per_volume_measure import VolumePerVolumeMeasure
from witsml21.volumetric_thermal_expansion_measure import VolumetricThermalExpansionMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimJobDiagnosticSession:
    """
    A pumping diagnostics session.

    :ivar name: The name of the session.
    :ivar number: The number of this pumping diagnostics session.
    :ivar description: A description of the session.
    :ivar choke_size: The size of the choke used during a flow back
        test.
    :ivar dtim_pump_on: The date and time pumping began.
    :ivar dtim_pump_off: The date and time pumping ended.
    :ivar pump_duration: The time between the shutin time and the pump
        on time.
    :ivar dtim_well_shutin: The date and time at which a well ceases
        flowing and the valves are closed.
    :ivar dtim_fracture_close: The date and time when the fluid in the
        fracture is completely leaked off into the formation and the
        fracture closes on its faces.
    :ivar avg_bottomhole_treatment_pres: Average bottomhole treatment
        pressure.
    :ivar avg_bottomhole_treatment_rate: Average bottomhole treatment
        flow rate.
    :ivar base_fluid_vol: Base fluid volume entering equipment.
    :ivar bottomhole_hydrostatic_pres: Bottomhole hydrostatic pressure.
    :ivar bubble_point_pres: The pressure at which gas begins to break
        out of an under saturated oil and form a free gas phase in the
        matrix or a gas cap.
    :ivar fluid_density: The density of the fluid.
    :ivar fracture_close_pres: The pressure when the fracture width
        becomes zero.
    :ivar friction_pres: The pressure loss due to fluid friction with
        the pipe while a fluid is being pumped.
    :ivar initial_shutin_pres: Initial shutin pressure.
    :ivar pore_pres: The pressure of the liquids in the formation pores.
    :ivar wellbore_volume: The volume of fluid in the wellbore.
    :ivar md_surface: The measured depth of the wellbore to its
        injection point.
    :ivar md_bottomhole: The measured depth of the bottom of the hole.
    :ivar md_mid_perforation: The measured depth of the middle
        perforation.
    :ivar tvd_mid_perforation: The true vertical depth of the middle
        perforation.
    :ivar surface_temperature: The constant earth temperature at a given
        depth specific to a region.
    :ivar bottomhole_temperature: Static bottomhole temperature.
    :ivar surface_fluid_temperature: Temperature of the fluid at the
        surface.
    :ivar fluid_compressibility: The volume change of a fluid when
        pressure is applied.
    :ivar reservoir_total_compressibility: The volume change of a
        reservoir material when pressure is applied.
    :ivar fluid_nprime_factor: Power law component. As 'n' decreases
        from 1, the fluid becomes more shear thinning. Reducing 'n'
        produces more non-Newtonian behavior.
    :ivar fluid_kprime_factor: The consistency index K is the shear
        stress or viscosity of the fluid at one sec-1 shear rate. An
        increasing K raises the effective viscosity.
    :ivar fluid_specific_heat: The heat required to raise one unit mass
        of a substance by one degree.
    :ivar fluid_thermal_conductivity: In physics, thermal conductivity
        is the property of a material describing its ability to conduct
        heat. It appears primarily in Fourier's Law for heat conduction.
        Thermal conductivity is measured in watts per kelvin-meter.
        Multiplied by a temperature difference (in kelvins) and an area
        (in square meters), and divided by a thickness (in meters), the
        thermal conductivity predicts the rate of energy loss (in watts)
        through a piece of material.
    :ivar fluid_thermal_expansion_coefficient: Dimensional response to
        temperature change is expressed by its coefficient of thermal
        expansion. When the temperature of a substance changes, the
        energy that is stored in the intermolecular bonds between atoms
        also changes. When the stored energy increases, so does the
        length of the molecular bonds. As a result, solids typically
        expand in response to heating and contract on cooling. The
        degree of expansion divided by the change in temperature is
        called the material's coefficient of thermal expansion and
        generally varies with temperature.
    :ivar fluid_efficiency: A measurement, derived from a data frac, of
        the efficiency of a particular fluid in creating fracture area
        on a particular formation at a set of conditions.
    :ivar foam_quality: Foam quality percentage of foam for the job
        during the stimulation services.
    :ivar percent_pad: The volume of the pad divided by the (volume of
        the pad + the volume of the proppant laden fluid).
    :ivar stage_number: The number of a stage associated with this
        diagnostics session.
    :ivar temperature_correction_applied: Are the calculations corrected
        for temperature? A value of "true" (or "1") indicates that the
        calculations were corrected for temperature. A value of "false"
        (or "0") or not given indicates otherwise.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar fluid_efficiency_test: A diagnostic test determining fluid
        efficiency.
    :ivar step_rate_test: An injection test, plotted pressure against
        injection rate, where a curve deflection and change of slope
        indicates the fracture breakdown pressure.
    :ivar step_down_test: An injection test involving multiple steps of
        injection rate and pressure, where a curve deflection and change
        of slope indicates the fracture breakdown pressure. An injection
        test involving multiple steps of injection rate and pressure,
        where a curve deflection and change of slope indicates the
        fracture breakdown pressure.
    :ivar pump_flow_back_test: A diagnostic test involving flowing a
        well back after treatment.
    :ivar uid: Unique identifier for this instance of
        StimJobDiagnosticSession.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_inclusive": 0,
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
    choke_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ChokeSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dtim_pump_on: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPumpOn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_pump_off: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPumpOff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    pump_duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "PumpDuration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dtim_well_shutin: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimWellShutin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_fracture_close: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimFractureClose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    avg_bottomhole_treatment_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgBottomholeTreatmentPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_bottomhole_treatment_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgBottomholeTreatmentRate",
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
    bottomhole_hydrostatic_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "BottomholeHydrostaticPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bubble_point_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "BubblePointPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidDensity",
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
    friction_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FrictionPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    initial_shutin_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "InitialShutinPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pore_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PorePres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wellbore_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WellboreVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_surface: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdSurface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_bottomhole: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdBottomhole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_mid_perforation: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdMidPerforation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_mid_perforation: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdMidPerforation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    surface_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "SurfaceTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bottomhole_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "BottomholeTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    surface_fluid_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "SurfaceFluidTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_compressibility: Optional[IsothermalCompressibilityMeasure] = field(
        default=None,
        metadata={
            "name": "FluidCompressibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    reservoir_total_compressibility: Optional[IsothermalCompressibilityMeasure] = field(
        default=None,
        metadata={
            "name": "ReservoirTotalCompressibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_nprime_factor: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "FluidNprimeFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_kprime_factor: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "FluidKprimeFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_specific_heat: Optional[SpecificHeatCapacityMeasure] = field(
        default=None,
        metadata={
            "name": "FluidSpecificHeat",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_thermal_conductivity: Optional[ThermalConductivityMeasure] = field(
        default=None,
        metadata={
            "name": "FluidThermalConductivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_thermal_expansion_coefficient: Optional[VolumetricThermalExpansionMeasure] = field(
        default=None,
        metadata={
            "name": "FluidThermalExpansionCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fluid_efficiency: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidEfficiency",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    foam_quality: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FoamQuality",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    percent_pad: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PercentPad",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stage_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "StageNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_inclusive": 0,
        }
    )
    temperature_correction_applied: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TemperatureCorrectionApplied",
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
    fluid_efficiency_test: List[StimFetTest] = field(
        default_factory=list,
        metadata={
            "name": "FluidEfficiencyTest",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    step_rate_test: List[StimStepTest] = field(
        default_factory=list,
        metadata={
            "name": "StepRateTest",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    step_down_test: List[StimStepDownTest] = field(
        default_factory=list,
        metadata={
            "name": "StepDownTest",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pump_flow_back_test: List[StimPumpFlowBackTest] = field(
        default_factory=list,
        metadata={
            "name": "PumpFlowBackTest",
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
