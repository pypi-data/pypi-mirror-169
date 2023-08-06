from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LengthMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
