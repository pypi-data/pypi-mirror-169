from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class StringMeasure:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        }
    )
    uom: Optional[UnitOfMeasure] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
