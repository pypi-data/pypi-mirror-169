from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.assembly import StringEquipment

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StringEquipmentSet:
    """
    Information on collection of set of equipment included in the string.
    """
    string_equipment: List[StringEquipment] = field(
        default_factory=list,
        metadata={
            "name": "StringEquipment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
