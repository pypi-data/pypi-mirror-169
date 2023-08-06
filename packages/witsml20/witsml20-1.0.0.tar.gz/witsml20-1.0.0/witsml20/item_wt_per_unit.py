from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_item_wt_or_vol_per_unit import AbstractItemWtOrVolPerUnit
from witsml20.mass_measure import MassMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ItemWtPerUnit(AbstractItemWtOrVolPerUnit):
    """
    Item weight per unit.

    :ivar item_wt_per_unit: Item weight per unit.
    """
    item_wt_per_unit: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "ItemWtPerUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
