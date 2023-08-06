from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.momentum_uom import MomentumUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MomentumMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MomentumUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
