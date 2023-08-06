from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.length_measure import LengthMeasure
from witsml21.measured_depth import MeasuredDepth

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TubularComponentOsduintegration:
    """
    Information about a TubularComponent that is relevant for OSDU integration
    but does not have a natural place in a TubularComponent.

    :ivar packer_set_depth_tvd: The depth the packer equipment was set
        to seal the casing or tubing.
    :ivar pilot_hole_size: Size of the Pilot Hole.
    :ivar section_type: Identifier of the Section Type.
    :ivar shoe_depth_tvd: Depth of the tubing shoe measured from the
        surface.
    :ivar tubular_component_base_md: The measured depth of the base from
        the specific component.
    :ivar tubular_component_base_reported_tvd: Depth of the base of the
        component measured from the Well-Head.
    :ivar tubular_component_bottom_connection_type: The Bottom
        Connection Type.
    :ivar tubular_component_box_pin_config: Type of collar used to
        couple the tubular with another tubing string.
    :ivar tubular_component_material_type: Specifies the material type
        constituting the component.
    :ivar tubular_component_top_connection_type: The Top Connection
        Type.
    :ivar tubular_component_top_md: The measured depth of the top from
        the specific component.
    :ivar tubular_component_top_reported_tvd: Depth of the top of the
        component measured from the Well-Head.
    """
    class Meta:
        name = "TubularComponentOSDUIntegration"

    packer_set_depth_tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "PackerSetDepthTvd",
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
    section_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    shoe_depth_tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "ShoeDepthTvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular_component_base_md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "TubularComponentBaseMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular_component_base_reported_tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TubularComponentBaseReportedTvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular_component_bottom_connection_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TubularComponentBottomConnectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    tubular_component_box_pin_config: Optional[str] = field(
        default=None,
        metadata={
            "name": "TubularComponentBoxPinConfig",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    tubular_component_material_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TubularComponentMaterialType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    tubular_component_top_connection_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TubularComponentTopConnectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    tubular_component_top_md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "TubularComponentTopMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular_component_top_reported_tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TubularComponentTopReportedTvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
