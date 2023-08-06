from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_item_wt_or_vol_per_unit import AbstractItemWtOrVolPerUnit
from witsml21.cost import Cost
from witsml21.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Inventory:
    """
    Inventory Component Schema.

    :ivar name: Name or type of inventory item.
    :ivar item_wt_or_vol_per_unit: Item weight or volume per unit.
    :ivar price_per_unit: Price per item unit, assume same currency for
        all items.
    :ivar qty_start: Start quantity for report interval.
    :ivar qty_adjustment: Daily quantity adjustment/correction.
    :ivar qty_received: Quantity received at the site.
    :ivar qty_returned: Quantity returned to base from site.
    :ivar qty_used: Quantity used for the report interval.
    :ivar cost_item: Cost for the product for the report interval.
    :ivar qty_on_location: Amount of the item remaining on location
        after all adjustments for the report interval.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Inventory.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    item_wt_or_vol_per_unit: Optional[AbstractItemWtOrVolPerUnit] = field(
        default=None,
        metadata={
            "name": "ItemWtOrVolPerUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    price_per_unit: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "PricePerUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    qty_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "QtyStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    qty_adjustment: Optional[float] = field(
        default=None,
        metadata={
            "name": "QtyAdjustment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    qty_received: Optional[float] = field(
        default=None,
        metadata={
            "name": "QtyReceived",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    qty_returned: Optional[float] = field(
        default=None,
        metadata={
            "name": "QtyReturned",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    qty_used: Optional[float] = field(
        default=None,
        metadata={
            "name": "QtyUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cost_item: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "CostItem",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    qty_on_location: Optional[float] = field(
        default=None,
        metadata={
            "name": "QtyOnLocation",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
