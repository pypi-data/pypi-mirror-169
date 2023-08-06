from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.length_per_pressure_uom import LengthPerPressureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LengthPerPressureMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[LengthPerPressureUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
