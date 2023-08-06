from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.luminous_efficacy_uom import LuminousEfficacyUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LuminousEfficacyMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LuminousEfficacyUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
