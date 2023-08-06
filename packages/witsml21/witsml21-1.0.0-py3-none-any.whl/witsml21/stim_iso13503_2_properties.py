from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.dimensionless_measure import DimensionlessMeasure
from witsml21.iso13503_2_crush_test_data import Iso135032CrushTestData
from witsml21.iso13503_2_sieve_analysis_data import Iso135032SieveAnalysisData
from witsml21.length_measure import LengthMeasure
from witsml21.mass_per_mass_measure import MassPerMassMeasure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimIso135032Properties:
    """
    ISO13503-2 properties.

    :ivar absolute_density: The density the material would have if no
        intra-granular porosity is present. (e.g. Boyle’s Law
        porosimetry).
    :ivar clusters_percent: Percentage of undesirable agglomerated
        discrete proppant particles which typically occurs more with
        inefficiently processed natural sand proppants as opposed to
        manufactured ceramic proppants. ISO 13503-2 and API RP19C limit
        the mass of clusters to less than 1%.
    :ivar kvalue: Crush test classification indicating the highest
        stress level at which a proppant generated no more than 10%
        crushed material rounded down to the nearest 1,000 psi during a
        crush test. For example, a value of 14 means ‘14K’ which is
        14000 psi.
    :ivar mean_particle_diameter: The mean diameter of particles in a
        sample of proppant.
    :ivar median_particle_diameter: The median diameter of particles in
        a sample of proppant.
    :ivar specific_gravity: Not formally part of ISO 13503.2 properties,
        the specific gravity is the apparent density of the proppant
        divided by the density of water.
    :ivar roundness: Krumbein Roundness Shape Factor that is a measure
        of the relative sharpness of grain corners or of grain
        curvature. Krumbein and Sloss (1963) are the most widely used
        method of determining shape factors.
    :ivar acid_solubility: The solubility of a proppant in 12:3 HCl:HF
        for 30 minutes at 150°F is an indication of the amount of
        soluble materials (i.e. carbonates, feldspars, iron oxides,
        clays, etc) present in the proppant.
    :ivar apparent_density: Apparent density excludes extra-granular
        porosity by placing a known mass in a volume of fluid and
        determining how much of the fluid is displaced (Archimedes).
    :ivar bulk_density: Bulk density includes both the proppant and the
        porosity. This is measured by filling a known volume with dry
        proppant and measuring the weight.
    :ivar loss_on_ignition: A mass loss (gravimetric) test method
        applied to coated proppants only, which determines the mass of
        resin coating applied to a natural sand or manufactured proppant
        by means of thorough combustion of the flammable resin from the
        nonflammable proppant. Reported as a % of original mass.
    :ivar sphericity: Krumbein Sphericity Shape Factor that is a measure
        of how closely a proppant particle approaches the shape of a
        sphere. Krumbein and Sloss (1963) are the most widely used
        method of determining shape factors.
    :ivar turbidity: A measure of water clarity, how much the material
        suspended in water decreases the passage of light through the
        water. Unit of measure may be Nephelometric Turbidity Unit
        (NTU), but may vary based upon the detector geometry.
    :ivar crush_test_data:
    :ivar sieve_analysis_data:
    :ivar uid: Unique identifier for this instance of
        StimISO13503_2Properties.
    """
    class Meta:
        name = "StimISO13503_2Properties"

    absolute_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AbsoluteDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    clusters_percent: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "ClustersPercent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    kvalue: Optional[float] = field(
        default=None,
        metadata={
            "name": "KValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mean_particle_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MeanParticleDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    median_particle_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MedianParticleDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    specific_gravity: Optional[float] = field(
        default=None,
        metadata={
            "name": "SpecificGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    roundness: Optional[float] = field(
        default=None,
        metadata={
            "name": "Roundness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    acid_solubility: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "AcidSolubility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    apparent_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "ApparentDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bulk_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BulkDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    loss_on_ignition: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "LossOnIgnition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sphericity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Sphericity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    turbidity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Turbidity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    crush_test_data: List[Iso135032CrushTestData] = field(
        default_factory=list,
        metadata={
            "name": "CrushTestData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sieve_analysis_data: List[Iso135032SieveAnalysisData] = field(
        default_factory=list,
        metadata={
            "name": "SieveAnalysisData",
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
