from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.area_per_area_measure import AreaPerAreaMeasure
from witsml21.citation import Citation
from witsml21.show_fluorescence import ShowFluorescence
from witsml21.show_level import ShowLevel
from witsml21.show_rating import ShowRating
from witsml21.show_speed import ShowSpeed

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CuttingsIntervalShow:
    """A set of measurements or observations on cuttings samples describing the
    evaluation of a hydrocarbon show based on observation of hydrocarbon
    staining and fluorescence.

    For information on procedures for show evaluation, see the WITSML
    Technical Usage Guide.

    :ivar citation: An ISO 19115 EIP-derived set of metadata attached to
        ensure the traceability of the CuttingsIntervalShow.
    :ivar show_rating: Show Rating.
    :ivar stain_color: Visible stain color.
    :ivar stain_distr: Visible stain distribution.
    :ivar stain_pc: Visible stain (commonly in percent).
    :ivar cut_speed: Cut speed.
    :ivar cut_color: Cut color.
    :ivar cut_strength: Cut strength.
    :ivar cut_form: Cut formulation.
    :ivar cut_level: Cut level (faint, bright, etc.).
    :ivar cut_flor_form: Cut fluorescence form.
    :ivar cut_flor_color: Cut fluorescence color.
    :ivar cut_flor_strength: Cut fluorescence strength.
    :ivar cut_flor_speed: Cut fluorescence speed.
    :ivar cut_flor_level: Cut fluorescence level.
    :ivar nat_flor_color: Natural fluorescence color.
    :ivar nat_flor_pc: Natural fluorescence (commonly in percent).
    :ivar nat_flor_level: Natural fluorescence level.
    :ivar nat_flor_desc: Natural fluorescence description.
    :ivar residue_color: Residue color.
    :ivar impregnated_litho: Impregnated lithology.
    :ivar odor: Description of any hydrocarbon type odors smelled.
    :ivar cutting_fluid: Description of the cutting solvent used to
        treat the cuttings.
    :ivar uid: Unique identifier for this instance of
        CuttingsIntervalShow.
    """
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    show_rating: Optional[ShowRating] = field(
        default=None,
        metadata={
            "name": "ShowRating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stain_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "StainColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    stain_distr: Optional[str] = field(
        default=None,
        metadata={
            "name": "StainDistr",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    stain_pc: Optional[AreaPerAreaMeasure] = field(
        default=None,
        metadata={
            "name": "StainPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cut_speed: Optional[ShowSpeed] = field(
        default=None,
        metadata={
            "name": "CutSpeed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cut_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "CutColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cut_strength: Optional[str] = field(
        default=None,
        metadata={
            "name": "CutStrength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cut_form: Optional[ShowLevel] = field(
        default=None,
        metadata={
            "name": "CutForm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cut_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "CutLevel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cut_flor_form: Optional[ShowLevel] = field(
        default=None,
        metadata={
            "name": "CutFlorForm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cut_flor_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "CutFlorColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cut_flor_strength: Optional[str] = field(
        default=None,
        metadata={
            "name": "CutFlorStrength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cut_flor_speed: Optional[ShowSpeed] = field(
        default=None,
        metadata={
            "name": "CutFlorSpeed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cut_flor_level: Optional[ShowFluorescence] = field(
        default=None,
        metadata={
            "name": "CutFlorLevel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nat_flor_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "NatFlorColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    nat_flor_pc: Optional[AreaPerAreaMeasure] = field(
        default=None,
        metadata={
            "name": "NatFlorPc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nat_flor_level: Optional[ShowFluorescence] = field(
        default=None,
        metadata={
            "name": "NatFlorLevel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nat_flor_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NatFlorDesc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    residue_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResidueColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    impregnated_litho: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImpregnatedLitho",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    odor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Odor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cutting_fluid: Optional[str] = field(
        default=None,
        metadata={
            "name": "CuttingFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
