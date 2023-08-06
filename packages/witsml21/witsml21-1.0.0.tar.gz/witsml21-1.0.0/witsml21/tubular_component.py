from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.angle_per_length_measure import AnglePerLengthMeasure
from witsml21.area_measure import AreaMeasure
from witsml21.bend import Bend
from witsml21.bit_record import BitRecord
from witsml21.box_pin_config import BoxPinConfig
from witsml21.connection import Connection
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.force_per_length_measure import ForcePerLengthMeasure
from witsml21.hole_opener import HoleOpener
from witsml21.jar import Jar
from witsml21.length_measure import LengthMeasure
from witsml21.length_per_length_measure import LengthPerLengthMeasure
from witsml21.mass_measure_ext import MassMeasureExt
from witsml21.mass_per_length_measure import MassPerLengthMeasure
from witsml21.material_type import MaterialType
from witsml21.moment_of_force_measure import MomentOfForceMeasure
from witsml21.motor import Motor
from witsml21.mwd_tool import MwdTool
from witsml21.name_tag import NameTag
from witsml21.nozzle import Nozzle
from witsml21.pressure_measure import PressureMeasure
from witsml21.pressure_measure_ext import PressureMeasureExt
from witsml21.rotary_steerable_tool import RotarySteerableTool
from witsml21.stabilizer import Stabilizer
from witsml21.tubular_component_osduintegration import TubularComponentOsduintegration
from witsml21.tubular_component_type import TubularComponentType
from witsml21.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TubularComponent:
    """Tubular Component Schema.

    Captures the order of the components in the XML instance,which is
    significant. The components are listed in the order in which they
    enter the hole. That is, the first component is the bit.

    :ivar manufacturer: Pointer to a BusinessAssociate representing the
        manufacturer of this component.
    :ivar nominal_diameter: Nominal size (diameter) of the component,
        e.g., 9.625", 12.25".
    :ivar nominal_weight: Nominal weight of the component
    :ivar supplier: Pointer to a BusinessAssociate representing the
        supplier for this component.
    :ivar tens_strength: Yield stress of steel - worn stress.
    :ivar tubular_component_osduintegration: Information about a
        TubularComponent that is relevant for OSDU integration but does
        not have a natural place in a TubularComponent.
    :ivar type_tubular_component: Type of component.
    :ivar sequence: The sequence within which the components entered the
        hole. That is, a sequence number of 1 entered first, 2 entered
        next, etc.
    :ivar description: Description of item and details.
    :ivar id: Internal diameter of object.
    :ivar od: Outside diameter of the body of the item.
    :ivar od_mx: Maximum outside diameter.
    :ivar len: Length of the item.
    :ivar len_joint_av: Average length of the joint for this string.
    :ivar num_joint_stand: Number of joints per stand of tubulars.
    :ivar wt_per_len: Weight per unit length.
    :ivar count: The count number of the same component.
    :ivar grade: Material grade for the tubular section.
    :ivar od_drift: Minimum pass through diameter.
    :ivar tens_yield: Yield stress of steel - worn stress.
    :ivar tq_yield: Torque at which yield occurs.
    :ivar stress_fatigue: Fatigue endurance limit.
    :ivar len_fishneck: Fish neck length.
    :ivar id_fishneck: Fish neck inside diameter.
    :ivar od_fishneck: Fish neck outside diameter.
    :ivar disp: Closed end displacement.
    :ivar pres_burst: Burst pressure.
    :ivar pres_collapse: Collapse pressure.
    :ivar class_service: Service class.
    :ivar wear_wall: Wall thickness wear (commonly in percent).
    :ivar thick_wall: Wall thickness.
    :ivar config_con: Box/Pin configuration.
    :ivar bend_stiffness: Bending stiffness of tubular.
    :ivar axial_stiffness: Axial stiffness of tubular.
    :ivar torsional_stiffness: Torsional stiffness of tubular.
    :ivar type_material: Type of material.
    :ivar dogleg_mx: Maximum dogleg severity.
    :ivar model: Component name from manufacturer.
    :ivar name_tag: An identification tag for the component tool. A
        serial number is a type of identification tag; however, some
        tags contain many pieces of information. This element only
        identifies the tag; it does not describe the contents.
    :ivar area_nozzle_flow: Total area of nozzles.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar connection:
    :ivar jar:
    :ivar mwd_tool:
    :ivar motor:
    :ivar stabilizer:
    :ivar bend:
    :ivar hole_opener:
    :ivar rotary_steerable_tool:
    :ivar bit_record:
    :ivar nozzle:
    :ivar uid: Unique identifier for this instance of TubularComponent
    """
    manufacturer: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nominal_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "NominalDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nominal_weight: Optional[MassMeasureExt] = field(
        default=None,
        metadata={
            "name": "NominalWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    supplier: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tens_strength: Optional[PressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "TensStrength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular_component_osduintegration: Optional[TubularComponentOsduintegration] = field(
        default=None,
        metadata={
            "name": "TubularComponentOSDUIntegration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_tubular_component: Optional[Union[TubularComponentType, str]] = field(
        default=None,
        metadata={
            "name": "TypeTubularComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
    id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    od_mx: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Len",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    len_joint_av: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenJointAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_joint_stand: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumJointStand",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wt_per_len: Optional[MassPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "WtPerLen",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grade: Optional[str] = field(
        default=None,
        metadata={
            "name": "Grade",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    od_drift: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdDrift",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tens_yield: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "TensYield",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_yield: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqYield",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stress_fatigue: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "StressFatigue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_fishneck: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenFishneck",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_fishneck: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdFishneck",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_fishneck: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdFishneck",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    disp: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Disp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_burst: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresBurst",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_collapse: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresCollapse",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    class_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassService",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    wear_wall: Optional[LengthPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "WearWall",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    thick_wall: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ThickWall",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    config_con: Optional[BoxPinConfig] = field(
        default=None,
        metadata={
            "name": "ConfigCon",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bend_stiffness: Optional[ForcePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "BendStiffness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    axial_stiffness: Optional[ForcePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "AxialStiffness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    torsional_stiffness: Optional[ForcePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "TorsionalStiffness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_material: Optional[MaterialType] = field(
        default=None,
        metadata={
            "name": "TypeMaterial",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dogleg_mx: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "DoglegMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    name_tag: List[NameTag] = field(
        default_factory=list,
        metadata={
            "name": "NameTag",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    area_nozzle_flow: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "AreaNozzleFlow",
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
    connection: List[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    jar: Optional[Jar] = field(
        default=None,
        metadata={
            "name": "Jar",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mwd_tool: Optional[MwdTool] = field(
        default=None,
        metadata={
            "name": "MwdTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    motor: Optional[Motor] = field(
        default=None,
        metadata={
            "name": "Motor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stabilizer: List[Stabilizer] = field(
        default_factory=list,
        metadata={
            "name": "Stabilizer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bend: List[Bend] = field(
        default_factory=list,
        metadata={
            "name": "Bend",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hole_opener: Optional[HoleOpener] = field(
        default=None,
        metadata={
            "name": "HoleOpener",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rotary_steerable_tool: Optional[RotarySteerableTool] = field(
        default=None,
        metadata={
            "name": "RotarySteerableTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bit_record: Optional[BitRecord] = field(
        default=None,
        metadata={
            "name": "BitRecord",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nozzle: List[Nozzle] = field(
        default_factory=list,
        metadata={
            "name": "Nozzle",
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
