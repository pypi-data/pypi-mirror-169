from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.assembly import StringEquipment

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StringAccessory:
    """StringAccessories contain the stringequipment's decorative components.

    An accessory is the stringEquipment or Strings’ decorative
    component.  An accessory is NOT directly screwed to the string. This
    part DOES NOT carry the weight of the rest of the String as opposed
    to the stringEquipment, which does. An Accessory is UNLIKE an
    Assembly on which the stringEquipment is built out of.
    """
    accessory: List[StringEquipment] = field(
        default_factory=list,
        metadata={
            "name": "Accessory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
