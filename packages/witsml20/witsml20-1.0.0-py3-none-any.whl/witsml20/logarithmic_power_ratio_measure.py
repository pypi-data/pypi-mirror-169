from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.logarithmic_power_ratio_uom import LogarithmicPowerRatioUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LogarithmicPowerRatioMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LogarithmicPowerRatioUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
