from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.citation import Citation
from witsml21.cuttings_interval_show import CuttingsIntervalShow
from witsml21.lithology_kind import LithologyKind
from witsml21.lithology_qualifier import LithologyQualifier
from witsml21.matrix_cement_kind import MatrixCementKind
from witsml21.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CuttingsIntervalLithology:
    """The description of a single rock type in this interval.

    Can include one or more CuttingsIntervalShow objects for hydrocarbon
    show evaluation of the individual lithology.

    :ivar kind: The geological name for the type of lithology from the
        enum table listing a subset of the OneGeology/CGI defined
        formation types.
    :ivar lith_pc: Lithology percent. Represents the portion of the
        sampled interval this lithology type relates to. The total of
        the lithologies within an interval should add up to 100 percent.
        If LithologySource in geology is: - "interpreted" only 100% is
        allowed. - "core" or "cuttings" then recommended usage is that
        the creating application uses blocks of 10%. i.e. 10, 20, 30,
        40, 50, 60, 70, 80, 90, 100. Ideally the input application
        should enforce a total of 100% for each defined depth interval.
        If the total for a depth interval does not add up to 100%, then
        use the "undifferentiated" code to fill out to 100%.
    :ivar citation: An ISO 19115 EIP-derived set of metadata attached to
        ensure the traceability of the CuttingsIntervalLithology.
    :ivar code_lith: An optional custom lithology encoding scheme. If
        used, it is recommended that the scheme follows the NPD required
        usage. With the numeric values noted in the enum tables, which
        was the original intent for this item. The NPD Coding System
        assigns a digital code to the main lithologies as per the
        Norwegian Blue Book data standards. The code was then derived by
        lithology = (main lithology * 10) + cement + (modifier / 100).
        Example: Calcite cemented silty micaceous sandstone: (33 * 10) +
        1 + (21 / 100) gives a numeric code of 331.21. However, the NPD
        is also working through Energistics/Caesar to potentially change
        this usage.) This scheme should not be used for mnemonics,
        because those vary by operator, and if an abbreviation is
        required, a local look-up table should be used by the rendering
        client, based on Lithology Type.
    :ivar color: STRUCTURED DESCRIPTION USAGE. Lithology color
        description, from Shell 1995 4.3.3.1 and 4.3.3.2 colors with the
        addition of: frosted. e.g., black, blue, brown, buff, green,
        grey, olive, orange, pink, purple, red, translucent, frosted,
        white, yellow; modified by: dark, light, moderate, medium,
        mottled, variegated, slight, weak, strong, and vivid.
    :ivar texture: STRUCTURED DESCRIPTION USAGE. Lithology matrix
        texture description from Shell 1995 4.3.2.6: crystalline, (often
        "feather-edge" appearance on breaking), friable, dull, earthy,
        chalky, (particle size less than 20m; often exhibits capillary
        imbibition) visibly particulate, granular, sucrosic, (often
        exhibits capillary imbibition). Examples: compact interlocking,
        particulate, (Gradational textures are quite common.) chalky
        matrix with sucrosic patches, (Composite textures also occur).
    :ivar hardness: STRUCTURED DESCRIPTION USAGE. Mineral hardness.
        Typically, this element is rarely used because mineral hardness
        is not typically recorded. What typically is recorded is
        compaction. However, this element is retained for use defined as
        per Mohs scale of mineral hardness.
    :ivar compaction: STRUCTURED DESCRIPTION USAGE. Lithology compaction
        from Shell 1995 4.3.1.5, which includes: not compacted, slightly
        compacted, compacted, strongly compacted, friable, indurated,
        hard.
    :ivar size_grain: STRUCTURED DESCRIPTION USAGE. Lithology grain size
        description. Defined from Shell 4.3.1.1.(Wentworth) modified to
        remove the ambiguous term pelite. Size ranges in millimeter (or
        micrometer) and inches. LT 256 mm        LT 10.1 in
        "boulder" 64-256 mm        2.5–10.1 in        "cobble"; 32–64 mm
        1.26–2.5 in       "very coarse gravel" 16–32 mm        0.63–1.26
        in        "coarse gravel" 8–16 mm            0.31–0.63 in
        "medium gravel" 4–8 mm            0.157–0.31 in        "fine
        gravel" 2–4 mm            0.079–0.157 in     "very fine gravel"
        1–2 mm           0.039–0.079 in    "very coarse sand" 0.5–1 mm
        0.020–0.039 in        "coarse sand" 0.25–0.5 mm
        0.010–0.020 in     "medium sand" 125–250 um        0.0049–0.010
        in        "fine sand" 62.5–125 um      .0025–0.0049 in   "very
        fine sand" 3.90625–62.5 um        0.00015–0.0025 in    "silt" LT
        3.90625 um        LT 0.00015 in        "clay" LT 1 um
        LT 0.000039 in        "colloid"
    :ivar roundness: STRUCTURED DESCRIPTION USAGE. Lithology roundness
        description from Shell 4.3.1.3. Roundness refers to modal size
        class: very angular, angular, subangular, subrounded, rounded,
        well rounded.
    :ivar sphericity: STRUCTURED DESCRIPTION USAGE. Lithology sphericity
        description for the modal size class of grains in the sample,
        defined as per Shell 4.3.1.4 Sphericity: very elongated,
        elongated, slightly elongated, slightly spherical, spherical,
        very spherical.
    :ivar sorting: STRUCTURED DESCRIPTION USAGE. Lithology sorting
        description from Shell 4.3.1.2 Sorting: very poorly sorted,
        unsorted, poorly sorted, poorly to moderately well sorted,
        moderately well sorted, well sorted, very well sorted,
        unimodally sorted, bimodally sorted.
    :ivar matrix_cement: STRUCTURED DESCRIPTION USAGE. Lithology
        matrix/cement description. Terms will be as defined in the
        enumeration table. e.g., "calcite" (Common) "dolomite",
        "ankerite" (e.g., North Sea HPHT reservoirs such as Elgin and
        Franklin have almost pure ankerite cementation) "siderite"
        (Sherwood sandstones, southern UK typical Siderite cements),
        "quartz" (grain-to-grain contact cementation or secondary quartz
        deposition), "kaolinite", "illite" (e.g., Village Fields North
        Sea), "smectite","chlorite" (Teg, Algeria.).
    :ivar porosity_visible: STRUCTURED DESCRIPTION USAGE. Lithology
        visible porosity description. Defined after BakerHughes
        definitions, as opposed to Shell, which has no linkage to actual
        numeric estimates. The theoretical maximum porosity for a
        clastic rock is about 26%, which is normally much reduced by
        other factors. When estimating porosities use: more than 15%
        "good"; 10 to 15% "fair"; 5 to 10% "poor"; less than 5% "trace";
        0 "none".
    :ivar porosity_fabric: STRUCTURED DESCRIPTION USAGE. Visible
        porosity fabric description from after Shell 4.3.2.1 and
        4.3.2.2: intergranular (particle size greater than 20m), fine
        interparticle (particle size less than 20m), intercrystalline,
        intragranular, intraskeletal, intracrystalline, mouldic,
        fenestral, shelter, framework, stylolitic, replacement,
        solution, vuggy, channel, cavernous.
    :ivar permeability: STRUCTURED DESCRIPTION USAGE. Lithology
        permeability description from Shell 4.3.2.5. In the future,
        these values would benefit from quantification, e.g., tight,
        slightly, fairly, highly.
    :ivar shows:
    :ivar qualifier:
    :ivar uid: Unique identifier for this instance of
        CuttingsIntervalLithology.
    """
    kind: Optional[Union[LithologyKind, str]] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    lith_pc: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "LithPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    code_lith: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeLith",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    texture: Optional[str] = field(
        default=None,
        metadata={
            "name": "Texture",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    hardness: Optional[str] = field(
        default=None,
        metadata={
            "name": "Hardness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    compaction: Optional[str] = field(
        default=None,
        metadata={
            "name": "Compaction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    size_grain: Optional[str] = field(
        default=None,
        metadata={
            "name": "SizeGrain",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    roundness: Optional[str] = field(
        default=None,
        metadata={
            "name": "Roundness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    sphericity: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sphericity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    sorting: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sorting",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    matrix_cement: Optional[MatrixCementKind] = field(
        default=None,
        metadata={
            "name": "MatrixCement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    porosity_visible: Optional[str] = field(
        default=None,
        metadata={
            "name": "PorosityVisible",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    porosity_fabric: Optional[str] = field(
        default=None,
        metadata={
            "name": "PorosityFabric",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    permeability: Optional[str] = field(
        default=None,
        metadata={
            "name": "Permeability",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    shows: List[CuttingsIntervalShow] = field(
        default_factory=list,
        metadata={
            "name": "Shows",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    qualifier: List[LithologyQualifier] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
