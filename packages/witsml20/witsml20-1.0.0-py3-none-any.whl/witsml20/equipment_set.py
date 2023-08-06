from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.equipment import Equipment

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class EquipmentSet:
    """
    Information on the collection of equipment.
    """
    equipment: List[Equipment] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
