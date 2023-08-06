from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.pressure_uom import PressureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PressureMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[PressureUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
