from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.pressure_per_time_uom import PressurePerTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressurePerTimeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PressurePerTimeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
