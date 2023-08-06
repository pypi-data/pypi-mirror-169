from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.normalized_power_uom import NormalizedPowerUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class NormalizedPowerMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[NormalizedPowerUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
