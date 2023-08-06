from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.electric_field_strength_uom import ElectricFieldStrengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectricFieldStrengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ElectricFieldStrengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
