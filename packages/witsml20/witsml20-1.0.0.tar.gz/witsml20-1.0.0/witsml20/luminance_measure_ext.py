from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.luminance_uom import LuminanceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LuminanceMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[LuminanceUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
