from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.cost import Cost
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.name_tag import NameTag

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DayCost:
    """Day Cost SchemaSchema.

    Captures daily cost information for the object (cost item) to which
    it is attached.

    :ivar num_afe: AFE number that this cost item applies to.
    :ivar cost_group: Cost group code.
    :ivar cost_class: Cost class code.
    :ivar cost_code: Cost code.
    :ivar cost_sub_code: Cost subcode.
    :ivar cost_item_description: Description of the cost item.
    :ivar item_kind: The kind of cost item specified (e.g., rig dayrate,
        joints casing).
    :ivar item_size: Size of one cost item.
    :ivar qty_item: Number of cost items used that day, e.g., 1 rig
        dayrate, 30 joints of casing.
    :ivar num_invoice: Invoice number for cost item; the  bill is sent
        to the operator.
    :ivar num_po: Purchase order number provided by the operator.
    :ivar num_ticket: The field ticket number issued by the service
        company on location.
    :ivar is_carry_over: Is this item carried from day to day? Values
        are "true" (or "1") and "false" (or "0").
    :ivar is_rental: Is this item a rental? Values are "true" (or "1")
        and "false" (or "0").
    :ivar name_tag: An identification tag for the item. A serial number
        is a type of identification tag; however, some tags contain many
        pieces of information. This element only identifies the tag and
        does not describe the contents.
    :ivar num_serial: Serial number.
    :ivar vendor: Pointer to a BusinessAssociate representing the
        vendor.
    :ivar num_vendor: Vendor number.
    :ivar pool: Name of pool/reservoir that this cost item can be
        accounted to.
    :ivar estimated: Is this an estimated cost? Values are "true" (or
        "1") and "false" (or "0").
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar cost_amount: Cost for the item for this record.
    :ivar cost_per_item: Cost of each cost item, assume same currency.
    :ivar uid: Unique identifier for this instance of DayCost
    """
    num_afe: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumAFE",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cost_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "CostGroup",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cost_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CostClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    cost_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CostCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    cost_sub_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CostSubCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cost_item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "CostItemDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    item_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 32,
        }
    )
    item_size: Optional[float] = field(
        default=None,
        metadata={
            "name": "ItemSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    qty_item: Optional[float] = field(
        default=None,
        metadata={
            "name": "QtyItem",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_invoice: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumInvoice",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    num_po: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumPO",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    num_ticket: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumTicket",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    is_carry_over: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCarryOver",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    is_rental: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRental",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    num_serial: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumSerial",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    vendor: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumVendor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    pool: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    estimated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Estimated",
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
    cost_amount: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "CostAmount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cost_per_item: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "CostPerItem",
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
