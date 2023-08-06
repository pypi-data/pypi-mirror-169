from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_item_wt_or_vol_per_unit import AbstractItemWtOrVolPerUnit
from witsml20.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ItemVolPerUnit(AbstractItemWtOrVolPerUnit):
    """
    Item volume per unit.

    :ivar item_vol_per_unit: Item volume per unit.
    """
    item_vol_per_unit: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "ItemVolPerUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
