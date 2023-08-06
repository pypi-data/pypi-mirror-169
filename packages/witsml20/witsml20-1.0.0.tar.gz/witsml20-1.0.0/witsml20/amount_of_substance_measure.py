from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.amount_of_substance_uom import AmountOfSubstanceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AmountOfSubstanceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AmountOfSubstanceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
