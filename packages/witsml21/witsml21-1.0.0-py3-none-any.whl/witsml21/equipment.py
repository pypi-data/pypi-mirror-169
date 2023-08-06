from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.coating import Coating
from witsml21.data_object_reference import DataObjectReference
from witsml21.equipment_type import EquipmentType
from witsml21.ext_prop_name_value import ExtPropNameValue
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.grade_type import GradeType
from witsml21.length_measure import LengthMeasure
from witsml21.mass_per_length_measure import MassPerLengthMeasure
from witsml21.perf_hole import PerfHole
from witsml21.perf_slot import PerfSlot

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Equipment:
    """Information on a piece of equipment.

    Each kind of equipment in the set has a type (what it is) and
    attributes common across all instances of that type of equipment.
    The String Equipment then references these common attributes.

    :ivar equipment_name: The name of the piece of equipment.
    :ivar equipment_type: The equipment type etc. bridge plug, bull
        plug. capillary tubing.
    :ivar manufacturer: Pointer to a BusinessAssociate representing the
        manufacturer of this equipment.
    :ivar model: The model of the equipment.
    :ivar catalog_id: Catalog where equipment can be found.
    :ivar catalog_name: Name of equipment as found in the catalog.
    :ivar brand_name: The equipment's brand name.
    :ivar model_type: The equipment's model type.
    :ivar series: Series number.
    :ivar is_serialized: A flag that indicates the equipment has a
        serial number.
    :ivar serial_number: Serial number.
    :ivar part_no: Number that identifies this part.
    :ivar surface_condition: Surface condition.
    :ivar material: Material that the equipment is made from.
    :ivar grade: Grade level of this piece of material.
    :ivar unit_weight: The weight per length of this equipment.
    :ivar coating_liner_applied: Flag indicating whether equipment has a
        coating.
    :ivar outside_coating: Equipment's outside coating based on
        enumeration value.
    :ivar inside_coating: Equipment's inner coating based on enumeration
        value.
    :ivar unit_length: The length of this equipment.
    :ivar major_od: The major outside diameter of this equipment.
    :ivar minor_od: The minor outside diameter of this equipment.
    :ivar od: The outside diameter of this equipment.
    :ivar max_od: The maximum outside diameter of this equipment.
    :ivar min_od: The minimum outside diameter of this equipment.
    :ivar major_id: The major inside diameter of this equipment.
    :ivar minor_id: The minor inside diameter of this equipment.
    :ivar id: The inside diameter of this equipment.
    :ivar max_id: The maximum inside diameter of this equipment.
    :ivar min_id: The minimum inside diameter of this equipment.
    :ivar drift: The drift diameter is the minimum inside diameter of
        pipe through which another tool or string can be pulled.
    :ivar nominal_size: The nominal size of this equipment.
    :ivar name_service: Sweet or sour service.
    :ivar description: The description of this equipment.
    :ivar description_permanent: The description of this equipment to be
        permanently kept.
    :ivar remark: Remarks about this equipment property.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar property:
    :ivar slot_as_manufactured:
    :ivar hole_as_manufactured:
    :ivar uid: Unique identifier for this instance of Equipment.
    """
    equipment_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    equipment_type: Optional[Union[EquipmentType, str]] = field(
        default=None,
        metadata={
            "name": "EquipmentType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    manufacturer: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
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
    catalog_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CatalogId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    catalog_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CatalogName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    brand_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    model_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModelType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "name": "Series",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    is_serialized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSerialized",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SerialNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    part_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartNo",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    surface_condition: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurfaceCondition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    material: Optional[str] = field(
        default=None,
        metadata={
            "name": "Material",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    grade: Optional[GradeType] = field(
        default=None,
        metadata={
            "name": "Grade",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    unit_weight: Optional[MassPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "UnitWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    coating_liner_applied: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CoatingLinerApplied",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    outside_coating: Optional[Coating] = field(
        default=None,
        metadata={
            "name": "OutsideCoating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    inside_coating: Optional[Coating] = field(
        default=None,
        metadata={
            "name": "InsideCoating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    unit_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "UnitLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    major_od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MajorOd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    minor_od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MinorOd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Od",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaxOd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    min_od: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MinOd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    major_id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MajorId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    minor_id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MinorId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaxId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    min_id: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MinId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    drift: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Drift",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nominal_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "NominalSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    name_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameService",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
    description_permanent: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescriptionPermanent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
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
    property: List[ExtPropNameValue] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    slot_as_manufactured: List[PerfSlot] = field(
        default_factory=list,
        metadata={
            "name": "SlotAsManufactured",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hole_as_manufactured: List[PerfHole] = field(
        default_factory=list,
        metadata={
            "name": "HoleAsManufactured",
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
