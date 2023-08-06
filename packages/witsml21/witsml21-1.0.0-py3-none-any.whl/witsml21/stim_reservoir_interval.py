from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.dimensionless_measure import DimensionlessMeasure
from witsml21.dynamic_viscosity_measure import DynamicViscosityMeasure
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.isothermal_compressibility_measure import IsothermalCompressibilityMeasure
from witsml21.length_measure import LengthMeasure
from witsml21.md_interval import MdInterval
from witsml21.permeability_rock_measure import PermeabilityRockMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimReservoirInterval:
    """
    Description of a reservoir interval.

    :ivar lith_md_interval: Lithology measured depth interval.
    :ivar lith_formation_permeability: Formation permeability, a
        measurement of the ability of a fluid to flow through a rock.
        Commonly measured in milliDarcys (1m2 = 0.000000000000986923
        Darcy).
    :ivar lith_youngs_modulus: Young's modulus (E) is a measure of the
        stiffness of an isotropic elastic material. It is also known as
        the Young modulus, modulus of elasticity, elastic modulus
        (though Young's modulus is actually one  of several elastic
        moduli such as the bulk modulus and the shear modulus) or
        tensile modulus. It is  defined as the ratio of the uniaxial
        stress over the uniaxial strain.
    :ivar lith_pore_pres: Refers to the pressure of fluids held within a
        soil or rock, in gaps between particles’ formation porosity.
    :ivar lith_net_pay_thickness: Net pay is computed. It is the
        thickness of rock that can deliver hydrocarbons to the wellbore
        formation.
    :ivar lith_name: A name for the formation lithology.
    :ivar gross_pay_md_interval: Measured depth of the bottom of the
        formation.
    :ivar gross_pay_thickness: The total thickness of the interval being
        treated, whether or not it is productive.
    :ivar net_pay_thickness: The thickness of the most productive part
        of the interval. Net pay is a subset of the gross.
    :ivar net_pay_pore_pres: The pore pressure of the net pay.
    :ivar net_pay_fluid_compressibility: The volume change of the fluid
        in the net pay when pressure is applied.
    :ivar net_pay_fluid_viscosity: With respect to the net pay, a
        measurement of the internal resistance of a fluid to flow
        against itself. Expressed as the ratio of shear stress to shear
        rate.
    :ivar net_pay_name: The name used for the net pay zone.
    :ivar net_pay_formation_permeability: The permeability of the net
        pay of the formation.
    :ivar lith_poissons_ratio: The ratio of the relative contraction
        strain, or transverse strain (normal to the applied load),
        divided by the relative extension strain, or axial strain (in
        the direction of the applied load).
    :ivar net_pay_formation_porosity: The porosity of the net pay
        formation.
    :ivar formation_permeability: Permeability of the formation.
    :ivar formation_porosity: Porosity of the formation.
    :ivar name_formation: Name of the formation.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        StimReservoirInterval
    """
    lith_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "LithMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lith_formation_permeability: Optional[PermeabilityRockMeasure] = field(
        default=None,
        metadata={
            "name": "LithFormationPermeability",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lith_youngs_modulus: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "LithYoungsModulus",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lith_pore_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "LithPorePres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lith_net_pay_thickness: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LithNetPayThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lith_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LithName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    gross_pay_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "GrossPayMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gross_pay_thickness: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "GrossPayThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    net_pay_thickness: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "NetPayThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    net_pay_pore_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "NetPayPorePres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    net_pay_fluid_compressibility: Optional[IsothermalCompressibilityMeasure] = field(
        default=None,
        metadata={
            "name": "NetPayFluidCompressibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    net_pay_fluid_viscosity: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "NetPayFluidViscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    net_pay_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetPayName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    net_pay_formation_permeability: Optional[PermeabilityRockMeasure] = field(
        default=None,
        metadata={
            "name": "NetPayFormationPermeability",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lith_poissons_ratio: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "LithPoissonsRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    net_pay_formation_porosity: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetPayFormationPorosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    formation_permeability: Optional[PermeabilityRockMeasure] = field(
        default=None,
        metadata={
            "name": "FormationPermeability",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    formation_porosity: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FormationPorosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    name_formation: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameFormation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
