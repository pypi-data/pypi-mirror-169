from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.length_measure import LengthMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.surf_equip_type import SurfEquipType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class SurfaceEquipment:
    """
    Rig Surface Equipment Schema.

    :ivar description: Description of item and details.
    :ivar pres_rating: Pressure rating of the item.
    :ivar type_surf_equip: Surface equipment type (IADC1-4, Custom,
        Coiled Tubing).
    :ivar use_pump_discharge: Use pump discharge line? Values are "true"
        (or "1") and "false" (or "0").
    :ivar use_standpipe: Use standpipe geometry? Values are "true" (or
        "1") and "false" (or "0").
    :ivar use_hose: Use kelly hose geometry? Values are "true" (or "1")
        and "false" (or "0").
    :ivar use_swivel: Use swivel geometry? Values are "true" (or "1")
        and "false" (or "0").
    :ivar use_kelly: Use kelly geometry? Values are "true" (or "1") and
        "false" (or "0").
    :ivar use_top_stack: Use top stack height? Values are "true" (or
        "1") and "false" (or "0").
    :ivar use_inj_stack: Use injector stack height? Values are "true"
        (or "1") and "false" (or "0").
    :ivar use_surface_iron: Use surface iron description? Values are
        "true" (or "1") and "false" (or "0").
    :ivar id_standpipe: Inner diameter of the standpipe.
    :ivar len_standpipe: Length of the standpipe.
    :ivar id_hose: Inner diameter of the kelly hose.
    :ivar len_hose: Length of the kelly hose.
    :ivar id_swivel: Inner diameter of the swivel.
    :ivar len_swivel: Length of the swivel.
    :ivar id_kelly: Inner diameter of the kelly bushing.
    :ivar len_kelly: Length of the kelly bushing.
    :ivar id_surface_iron: Inner diameter of the surface iron.
    :ivar len_surface_iron: Length of the surface iron.
    :ivar ht_surface_iron: Height of the surface iron.
    :ivar id_discharge_line: Coiled tubing: inner diameter of the pump
        discharge line.
    :ivar len_discharge_line: Coiled tubing: length of the pump
        discharge line.
    :ivar ct_wrap_type: Coiled tubing: the coiled tubing wrap type.
    :ivar od_reel: Coiled tubing: outside diameter of the coiled tubing
        reel.
    :ivar od_core: Coiled tubing: outside diameter of the reel core that
        the coiled tubing is wrapped around.
    :ivar wid_reel_wrap: Coiled tubing: width of the reel core. This is
        the inside dimension.
    :ivar len_reel: Coiled tubing: length of the coiled tubing remaining
        on the reel.
    :ivar inj_stk_up: Coiled tubing: Does it have an injector stack up?
        Values are "true" (or "1") and "false" (or "0").
    :ivar ht_inj_stk: Coiled tubing: The length of tubing from the end
        of the coil reel to the rotary kelly bushing. This length
        includes the tubing in the hole and the tubing on the reel. This
        measurement takes into account the 20 or so feet of tubing that
        is being straightened and pushed through the injector head.
    :ivar umb_inside: Coiled tubing: Umbilical inside, true/false flag
        to account for the wireline inside the coiled tubing. With this
        pressure loss calculation, you can calculate for the strings
        used for logging, wireline coring, etc. Values are "true" (or
        "1") and "false" (or "0").
    :ivar od_umbilical: Coiled tubing: outer diameter of the umbilical.
    :ivar len_umbilical: Coiled tubing: length of the umbilical.
    :ivar id_top_stk: Top drive: inner diameter of the top stack.
    :ivar ht_top_stk: Top drive: The distance that the mud travels from
        the end of the standpipe hose to the drill pipe connection at
        the bottom of the top drive. We are measuring the distance that
        the mud will flow through the top drive.For the top drive. The
        distance that the mud travels from the end of the standpipe hose
        to the drill pipe connection at the bottom of the top drive.
        This is the measurement of the distance that the mud flows
        through the top drive.
    :ivar ht_flange: Height of the flange.
    """
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    pres_rating: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresRating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_surf_equip: Optional[SurfEquipType] = field(
        default=None,
        metadata={
            "name": "TypeSurfEquip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    use_pump_discharge: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsePumpDischarge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    use_standpipe: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseStandpipe",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    use_hose: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseHose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    use_swivel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseSwivel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    use_kelly: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseKelly",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    use_top_stack: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseTopStack",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    use_inj_stack: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseInjStack",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    use_surface_iron: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseSurfaceIron",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_standpipe: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdStandpipe",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_standpipe: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenStandpipe",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_hose: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdHose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_hose: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenHose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_swivel: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdSwivel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_swivel: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenSwivel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_kelly: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdKelly",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_kelly: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenKelly",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_surface_iron: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdSurfaceIron",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_surface_iron: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenSurfaceIron",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ht_surface_iron: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HtSurfaceIron",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_discharge_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdDischargeLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_discharge_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenDischargeLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ct_wrap_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtWrapType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    od_reel: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdReel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_core: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdCore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wid_reel_wrap: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "WidReelWrap",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_reel: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenReel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    inj_stk_up: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InjStkUp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ht_inj_stk: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HtInjStk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    umb_inside: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UmbInside",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_umbilical: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdUmbilical",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_umbilical: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenUmbilical",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_top_stk: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdTopStk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ht_top_stk: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HtTopStk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ht_flange: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HtFlange",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
