from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class QuantityTypeKind(Enum):
    """
    :cvar ABSORBED_DOSE:
    :cvar ACTIVITY_OF_RADIOACTIVITY:
    :cvar ACTIVITY_OF_RADIOACTIVITY_PER_VOLUME:
    :cvar AMOUNT_OF_SUBSTANCE:
    :cvar AMOUNT_OF_SUBSTANCE_PER_AMOUNT_OF_SUBSTANCE:
    :cvar AMOUNT_OF_SUBSTANCE_PER_AREA:
    :cvar AMOUNT_OF_SUBSTANCE_PER_TIME:
    :cvar AMOUNT_OF_SUBSTANCE_PER_TIME_PER_AREA:
    :cvar AMOUNT_OF_SUBSTANCE_PER_VOLUME:
    :cvar ANGLE_PER_LENGTH:
    :cvar ANGLE_PER_VOLUME:
    :cvar ANGULAR_ACCELERATION:
    :cvar ANGULAR_VELOCITY:
    :cvar API_GAMMA_RAY:
    :cvar API_GRAVITY:
    :cvar API_NEUTRON:
    :cvar AREA:
    :cvar AREA_PER_AMOUNT_OF_SUBSTANCE:
    :cvar AREA_PER_AREA:
    :cvar AREA_PER_COUNT:
    :cvar AREA_PER_MASS:
    :cvar AREA_PER_TIME:
    :cvar AREA_PER_VOLUME:
    :cvar ATTENUATION_PER_FREQUENCY_INTERVAL:
    :cvar CAPACITANCE:
    :cvar CATION_EXCHANGE_CAPACITY:
    :cvar DATA_TRANSFER_SPEED:
    :cvar DIFFUSION_COEFFICIENT:
    :cvar DIFFUSIVE_TIME_OF_FLIGHT:
    :cvar DIGITAL_STORAGE:
    :cvar DIMENSIONLESS:
    :cvar DIPOLE_MOMENT:
    :cvar DOSE_EQUIVALENT:
    :cvar DYNAMIC_VISCOSITY:
    :cvar ELECTRIC_CHARGE:
    :cvar ELECTRIC_CHARGE_PER_AREA:
    :cvar ELECTRIC_CHARGE_PER_MASS:
    :cvar ELECTRIC_CHARGE_PER_VOLUME:
    :cvar ELECTRIC_CONDUCTANCE:
    :cvar ELECTRIC_CONDUCTIVITY:
    :cvar ELECTRIC_CURRENT:
    :cvar ELECTRIC_CURRENT_DENSITY:
    :cvar ELECTRIC_FIELD_STRENGTH:
    :cvar ELECTRIC_POTENTIAL_DIFFERENCE:
    :cvar ELECTRIC_RESISTANCE:
    :cvar ELECTRIC_RESISTANCE_PER_LENGTH:
    :cvar ELECTRICAL_RESISTIVITY:
    :cvar ELECTROMAGNETIC_MOMENT:
    :cvar ENERGY:
    :cvar ENERGY_LENGTH_PER_AREA:
    :cvar ENERGY_LENGTH_PER_TIME_AREA_TEMPERATURE:
    :cvar ENERGY_PER_AREA:
    :cvar ENERGY_PER_LENGTH:
    :cvar ENERGY_PER_MASS:
    :cvar ENERGY_PER_MASS_PER_TIME:
    :cvar ENERGY_PER_VOLUME:
    :cvar FORCE:
    :cvar FORCE_AREA:
    :cvar FORCE_LENGTH_PER_LENGTH:
    :cvar FORCE_PER_FORCE:
    :cvar FORCE_PER_LENGTH:
    :cvar FORCE_PER_VOLUME:
    :cvar FREQUENCY:
    :cvar FREQUENCY_INTERVAL:
    :cvar HEAT_CAPACITY:
    :cvar HEAT_FLOW_RATE:
    :cvar HEAT_TRANSFER_COEFFICIENT:
    :cvar ILLUMINANCE:
    :cvar INDUCTANCE:
    :cvar ISOTHERMAL_COMPRESSIBILITY:
    :cvar KINEMATIC_VISCOSITY:
    :cvar LENGTH:
    :cvar LENGTH_PER_LENGTH:
    :cvar LENGTH_PER_MASS:
    :cvar LENGTH_PER_PRESSURE:
    :cvar LENGTH_PER_TEMPERATURE:
    :cvar LENGTH_PER_TIME:
    :cvar LENGTH_PER_VOLUME:
    :cvar LIGHT_EXPOSURE:
    :cvar LINEAR_ACCELERATION:
    :cvar LINEAR_THERMAL_EXPANSION:
    :cvar LOGARITHMIC_POWER_RATIO:
    :cvar LOGARITHMIC_POWER_RATIO_PER_LENGTH:
    :cvar LUMINANCE:
    :cvar LUMINOUS_EFFICACY:
    :cvar LUMINOUS_FLUX:
    :cvar LUMINOUS_INTENSITY:
    :cvar MAGNETIC_DIPOLE_MOMENT:
    :cvar MAGNETIC_FIELD_STRENGTH:
    :cvar MAGNETIC_FLUX:
    :cvar MAGNETIC_FLUX_DENSITY:
    :cvar MAGNETIC_FLUX_DENSITY_PER_LENGTH:
    :cvar MAGNETIC_PERMEABILITY:
    :cvar MAGNETIC_VECTOR_POTENTIAL:
    :cvar MASS:
    :cvar MASS_LENGTH:
    :cvar MASS_PER_AREA:
    :cvar MASS_PER_ENERGY:
    :cvar MASS_PER_LENGTH:
    :cvar MASS_PER_MASS:
    :cvar MASS_PER_TIME:
    :cvar MASS_PER_TIME_PER_AREA:
    :cvar MASS_PER_TIME_PER_LENGTH:
    :cvar MASS_PER_VOLUME:
    :cvar MASS_PER_VOLUME_PER_LENGTH:
    :cvar MASS_PER_VOLUME_PER_PRESSURE:
    :cvar MASS_PER_VOLUME_PER_TEMPERATURE:
    :cvar MOBILITY:
    :cvar MOLAR_ENERGY:
    :cvar MOLAR_HEAT_CAPACITY:
    :cvar MOLAR_VOLUME:
    :cvar MOLECULAR_WEIGHT:
    :cvar MOMENT_OF_FORCE:
    :cvar MOMENT_OF_INERTIA:
    :cvar MOMENTUM:
    :cvar NORMALIZED_POWER:
    :cvar PRESSURE_PER_FLOWRATE:
    :cvar PRESSURE_PER_FLOWRATE_SQUARED:
    :cvar PERMEABILITY_LENGTH:
    :cvar PERMEABILITY_ROCK:
    :cvar PERMITTIVITY:
    :cvar PLANE_ANGLE:
    :cvar POTENTIAL_DIFFERENCE_PER_POWER_DROP:
    :cvar POWER:
    :cvar POWER_PER_AREA:
    :cvar POWER_PER_POWER:
    :cvar POWER_PER_VOLUME:
    :cvar PRESSURE:
    :cvar PRESSURE_PER_PRESSURE:
    :cvar PRESSURE_PER_TIME:
    :cvar PRESSURE_PER_VOLUME:
    :cvar PRESSURE_SQUARED:
    :cvar PRESSURE_SQUARED_PER_FORCE_TIME_PER_AREA:
    :cvar PRESSURE_TIME_PER_VOLUME:
    :cvar QUANTITY_OF_LIGHT:
    :cvar RADIANCE:
    :cvar RADIANT_INTENSITY:
    :cvar RECIPROCAL_AREA:
    :cvar RECIPROCAL_ELECTRIC_POTENTIAL_DIFFERENCE:
    :cvar RECIPROCAL_FORCE:
    :cvar RECIPROCAL_LENGTH:
    :cvar RECIPROCAL_MASS:
    :cvar RECIPROCAL_MASS_TIME:
    :cvar RECIPROCAL_PRESSURE:
    :cvar RECIPROCAL_TIME:
    :cvar RECIPROCAL_VOLUME:
    :cvar RELUCTANCE:
    :cvar SECOND_MOMENT_OF_AREA:
    :cvar SIGNALING_EVENT_PER_TIME:
    :cvar SOLID_ANGLE:
    :cvar SPECIFIC_HEAT_CAPACITY:
    :cvar TEMPERATURE_INTERVAL:
    :cvar TEMPERATURE_INTERVAL_PER_LENGTH:
    :cvar TEMPERATURE_INTERVAL_PER_PRESSURE:
    :cvar TEMPERATURE_INTERVAL_PER_TIME:
    :cvar THERMAL_CONDUCTANCE:
    :cvar THERMAL_CONDUCTIVITY:
    :cvar THERMAL_DIFFUSIVITY:
    :cvar THERMAL_INSULANCE:
    :cvar THERMAL_RESISTANCE:
    :cvar THERMODYNAMIC_TEMPERATURE:
    :cvar THERMODYNAMIC_TEMPERATURE_PER_THERMODYNAMIC_TEMPERATURE:
    :cvar TIME:
    :cvar TIME_PER_LENGTH:
    :cvar TIME_PER_MASS:
    :cvar TIME_PER_TIME:
    :cvar TIME_PER_VOLUME:
    :cvar VERTICAL_COORDINATE:
    :cvar VOLUME:
    :cvar VOLUME_FLOW_RATE_PER_VOLUME_FLOW_RATE:
    :cvar VOLUME_PER_AREA:
    :cvar VOLUME_PER_LENGTH:
    :cvar VOLUME_PER_MASS:
    :cvar VOLUME_PER_PRESSURE:
    :cvar VOLUME_PER_ROTATION:
    :cvar VOLUME_PER_TIME:
    :cvar VOLUME_PER_TIME_LENGTH:
    :cvar VOLUME_PER_TIME_PER_AREA:
    :cvar VOLUME_PER_TIME_PER_LENGTH:
    :cvar VOLUME_PER_TIME_PER_PRESSURE:
    :cvar VOLUME_PER_TIME_PER_PRESSURE_LENGTH:
    :cvar VOLUME_PER_TIME_PER_TIME:
    :cvar VOLUME_PER_TIME_PER_VOLUME:
    :cvar VOLUME_PER_VOLUME:
    :cvar VOLUMETRIC_HEAT_TRANSFER_COEFFICIENT:
    :cvar VOLUMETRIC_THERMAL_EXPANSION:
    :cvar UNITLESS: A unitless quantity is a quantity which has no unit
        of measure symbol, but could be a real physical measurement.
        Examples would be a count, pH, wire gauge (AWG and BWG) and shoe
        size. This is different from a dimensionless quantity which
        represents a ratio whose units of measure have cancelled each
        other. DImensionless quantities can have units of measure (like
        ppm or %) or may not have a displayable unit of measure symbol
        (in which case the units symbol Euc is used in a data transfer).
        Units derived from a unitless number simply ignore the unitless
        part. For example, the unit for counts per hour is just inverse
        hours (1/hr).
    :cvar NOT_A_MEASURE: The "not a measure" quantity class represents
        data values which are not measures at all. This would include
        strings, ordinal numbers, index values and other things for
        which the concept of units of measure is irrelevant.
    """
    ABSORBED_DOSE = "absorbed dose"
    ACTIVITY_OF_RADIOACTIVITY = "activity of radioactivity"
    ACTIVITY_OF_RADIOACTIVITY_PER_VOLUME = "activity of radioactivity per volume"
    AMOUNT_OF_SUBSTANCE = "amount of substance"
    AMOUNT_OF_SUBSTANCE_PER_AMOUNT_OF_SUBSTANCE = "amount of substance per amount of substance"
    AMOUNT_OF_SUBSTANCE_PER_AREA = "amount of substance per area"
    AMOUNT_OF_SUBSTANCE_PER_TIME = "amount of substance per time"
    AMOUNT_OF_SUBSTANCE_PER_TIME_PER_AREA = "amount of substance per time per area"
    AMOUNT_OF_SUBSTANCE_PER_VOLUME = "amount of substance per volume"
    ANGLE_PER_LENGTH = "angle per length"
    ANGLE_PER_VOLUME = "angle per volume"
    ANGULAR_ACCELERATION = "angular acceleration"
    ANGULAR_VELOCITY = "angular velocity"
    API_GAMMA_RAY = "api gamma ray"
    API_GRAVITY = "api gravity"
    API_NEUTRON = "api neutron"
    AREA = "area"
    AREA_PER_AMOUNT_OF_SUBSTANCE = "area per amount of substance"
    AREA_PER_AREA = "area per area"
    AREA_PER_COUNT = "area per count"
    AREA_PER_MASS = "area per mass"
    AREA_PER_TIME = "area per time"
    AREA_PER_VOLUME = "area per volume"
    ATTENUATION_PER_FREQUENCY_INTERVAL = "attenuation per frequency interval"
    CAPACITANCE = "capacitance"
    CATION_EXCHANGE_CAPACITY = "cation exchange capacity"
    DATA_TRANSFER_SPEED = "data transfer speed"
    DIFFUSION_COEFFICIENT = "diffusion coefficient"
    DIFFUSIVE_TIME_OF_FLIGHT = "diffusive time of flight"
    DIGITAL_STORAGE = "digital storage"
    DIMENSIONLESS = "dimensionless"
    DIPOLE_MOMENT = "dipole moment"
    DOSE_EQUIVALENT = "dose equivalent"
    DYNAMIC_VISCOSITY = "dynamic viscosity"
    ELECTRIC_CHARGE = "electric charge"
    ELECTRIC_CHARGE_PER_AREA = "electric charge per area"
    ELECTRIC_CHARGE_PER_MASS = "electric charge per mass"
    ELECTRIC_CHARGE_PER_VOLUME = "electric charge per volume"
    ELECTRIC_CONDUCTANCE = "electric conductance"
    ELECTRIC_CONDUCTIVITY = "electric conductivity"
    ELECTRIC_CURRENT = "electric current"
    ELECTRIC_CURRENT_DENSITY = "electric current density"
    ELECTRIC_FIELD_STRENGTH = "electric field strength"
    ELECTRIC_POTENTIAL_DIFFERENCE = "electric potential difference"
    ELECTRIC_RESISTANCE = "electric resistance"
    ELECTRIC_RESISTANCE_PER_LENGTH = "electric resistance per length"
    ELECTRICAL_RESISTIVITY = "electrical resistivity"
    ELECTROMAGNETIC_MOMENT = "electromagnetic moment"
    ENERGY = "energy"
    ENERGY_LENGTH_PER_AREA = "energy length per area"
    ENERGY_LENGTH_PER_TIME_AREA_TEMPERATURE = "energy length per time area temperature"
    ENERGY_PER_AREA = "energy per area"
    ENERGY_PER_LENGTH = "energy per length"
    ENERGY_PER_MASS = "energy per mass"
    ENERGY_PER_MASS_PER_TIME = "energy per mass per time"
    ENERGY_PER_VOLUME = "energy per volume"
    FORCE = "force"
    FORCE_AREA = "force area"
    FORCE_LENGTH_PER_LENGTH = "force length per length"
    FORCE_PER_FORCE = "force per force"
    FORCE_PER_LENGTH = "force per length"
    FORCE_PER_VOLUME = "force per volume"
    FREQUENCY = "frequency"
    FREQUENCY_INTERVAL = "frequency interval"
    HEAT_CAPACITY = "heat capacity"
    HEAT_FLOW_RATE = "heat flow rate"
    HEAT_TRANSFER_COEFFICIENT = "heat transfer coefficient"
    ILLUMINANCE = "illuminance"
    INDUCTANCE = "inductance"
    ISOTHERMAL_COMPRESSIBILITY = "isothermal compressibility"
    KINEMATIC_VISCOSITY = "kinematic viscosity"
    LENGTH = "length"
    LENGTH_PER_LENGTH = "length per length"
    LENGTH_PER_MASS = "length per mass"
    LENGTH_PER_PRESSURE = "length per pressure"
    LENGTH_PER_TEMPERATURE = "length per temperature"
    LENGTH_PER_TIME = "length per time"
    LENGTH_PER_VOLUME = "length per volume"
    LIGHT_EXPOSURE = "light exposure"
    LINEAR_ACCELERATION = "linear acceleration"
    LINEAR_THERMAL_EXPANSION = "linear thermal expansion"
    LOGARITHMIC_POWER_RATIO = "logarithmic power ratio"
    LOGARITHMIC_POWER_RATIO_PER_LENGTH = "logarithmic power ratio per length"
    LUMINANCE = "luminance"
    LUMINOUS_EFFICACY = "luminous efficacy"
    LUMINOUS_FLUX = "luminous flux"
    LUMINOUS_INTENSITY = "luminous intensity"
    MAGNETIC_DIPOLE_MOMENT = "magnetic dipole moment"
    MAGNETIC_FIELD_STRENGTH = "magnetic field strength"
    MAGNETIC_FLUX = "magnetic flux"
    MAGNETIC_FLUX_DENSITY = "magnetic flux density"
    MAGNETIC_FLUX_DENSITY_PER_LENGTH = "magnetic flux density per length"
    MAGNETIC_PERMEABILITY = "magnetic permeability"
    MAGNETIC_VECTOR_POTENTIAL = "magnetic vector potential"
    MASS = "mass"
    MASS_LENGTH = "mass length"
    MASS_PER_AREA = "mass per area"
    MASS_PER_ENERGY = "mass per energy"
    MASS_PER_LENGTH = "mass per length"
    MASS_PER_MASS = "mass per mass"
    MASS_PER_TIME = "mass per time"
    MASS_PER_TIME_PER_AREA = "mass per time per area"
    MASS_PER_TIME_PER_LENGTH = "mass per time per length"
    MASS_PER_VOLUME = "mass per volume"
    MASS_PER_VOLUME_PER_LENGTH = "mass per volume per length"
    MASS_PER_VOLUME_PER_PRESSURE = "mass per volume per pressure"
    MASS_PER_VOLUME_PER_TEMPERATURE = "mass per volume per temperature"
    MOBILITY = "mobility"
    MOLAR_ENERGY = "molar energy"
    MOLAR_HEAT_CAPACITY = "molar heat capacity"
    MOLAR_VOLUME = "molar volume"
    MOLECULAR_WEIGHT = "molecular weight"
    MOMENT_OF_FORCE = "moment of force"
    MOMENT_OF_INERTIA = "moment of inertia"
    MOMENTUM = "momentum"
    NORMALIZED_POWER = "normalized power"
    PRESSURE_PER_FLOWRATE = "pressure per flowrate"
    PRESSURE_PER_FLOWRATE_SQUARED = "pressure per flowrate squared"
    PERMEABILITY_LENGTH = "permeability length"
    PERMEABILITY_ROCK = "permeability rock"
    PERMITTIVITY = "permittivity"
    PLANE_ANGLE = "plane angle"
    POTENTIAL_DIFFERENCE_PER_POWER_DROP = "potential difference per power drop"
    POWER = "power"
    POWER_PER_AREA = "power per area"
    POWER_PER_POWER = "power per power"
    POWER_PER_VOLUME = "power per volume"
    PRESSURE = "pressure"
    PRESSURE_PER_PRESSURE = "pressure per pressure"
    PRESSURE_PER_TIME = "pressure per time"
    PRESSURE_PER_VOLUME = "pressure per volume"
    PRESSURE_SQUARED = "pressure squared"
    PRESSURE_SQUARED_PER_FORCE_TIME_PER_AREA = "pressure squared per force time per area"
    PRESSURE_TIME_PER_VOLUME = "pressure time per volume"
    QUANTITY_OF_LIGHT = "quantity of light"
    RADIANCE = "radiance"
    RADIANT_INTENSITY = "radiant intensity"
    RECIPROCAL_AREA = "reciprocal area"
    RECIPROCAL_ELECTRIC_POTENTIAL_DIFFERENCE = "reciprocal electric potential difference"
    RECIPROCAL_FORCE = "reciprocal force"
    RECIPROCAL_LENGTH = "reciprocal length"
    RECIPROCAL_MASS = "reciprocal mass"
    RECIPROCAL_MASS_TIME = "reciprocal mass time"
    RECIPROCAL_PRESSURE = "reciprocal pressure"
    RECIPROCAL_TIME = "reciprocal time"
    RECIPROCAL_VOLUME = "reciprocal volume"
    RELUCTANCE = "reluctance"
    SECOND_MOMENT_OF_AREA = "second moment of area"
    SIGNALING_EVENT_PER_TIME = "signaling event per time"
    SOLID_ANGLE = "solid angle"
    SPECIFIC_HEAT_CAPACITY = "specific heat capacity"
    TEMPERATURE_INTERVAL = "temperature interval"
    TEMPERATURE_INTERVAL_PER_LENGTH = "temperature interval per length"
    TEMPERATURE_INTERVAL_PER_PRESSURE = "temperature interval per pressure"
    TEMPERATURE_INTERVAL_PER_TIME = "temperature interval per time"
    THERMAL_CONDUCTANCE = "thermal conductance"
    THERMAL_CONDUCTIVITY = "thermal conductivity"
    THERMAL_DIFFUSIVITY = "thermal diffusivity"
    THERMAL_INSULANCE = "thermal insulance"
    THERMAL_RESISTANCE = "thermal resistance"
    THERMODYNAMIC_TEMPERATURE = "thermodynamic temperature"
    THERMODYNAMIC_TEMPERATURE_PER_THERMODYNAMIC_TEMPERATURE = "thermodynamic temperature per thermodynamic temperature"
    TIME = "time"
    TIME_PER_LENGTH = "time per length"
    TIME_PER_MASS = "time per mass"
    TIME_PER_TIME = "time per time"
    TIME_PER_VOLUME = "time per volume"
    VERTICAL_COORDINATE = "vertical coordinate"
    VOLUME = "volume"
    VOLUME_FLOW_RATE_PER_VOLUME_FLOW_RATE = "volume flow rate per volume flow rate"
    VOLUME_PER_AREA = "volume per area"
    VOLUME_PER_LENGTH = "volume per length"
    VOLUME_PER_MASS = "volume per mass"
    VOLUME_PER_PRESSURE = "volume per pressure"
    VOLUME_PER_ROTATION = "volume per rotation"
    VOLUME_PER_TIME = "volume per time"
    VOLUME_PER_TIME_LENGTH = "volume per time length"
    VOLUME_PER_TIME_PER_AREA = "volume per time per area"
    VOLUME_PER_TIME_PER_LENGTH = "volume per time per length"
    VOLUME_PER_TIME_PER_PRESSURE = "volume per time per pressure"
    VOLUME_PER_TIME_PER_PRESSURE_LENGTH = "volume per time per pressure length"
    VOLUME_PER_TIME_PER_TIME = "volume per time per time"
    VOLUME_PER_TIME_PER_VOLUME = "volume per time per volume"
    VOLUME_PER_VOLUME = "volume per volume"
    VOLUMETRIC_HEAT_TRANSFER_COEFFICIENT = "volumetric heat transfer coefficient"
    VOLUMETRIC_THERMAL_EXPANSION = "volumetric thermal expansion"
    UNITLESS = "unitless"
    NOT_A_MEASURE = "not a measure"
