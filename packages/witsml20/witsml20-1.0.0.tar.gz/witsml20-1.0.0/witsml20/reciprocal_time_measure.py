from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.reciprocal_time_uom import ReciprocalTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReciprocalTimeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ReciprocalTimeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
