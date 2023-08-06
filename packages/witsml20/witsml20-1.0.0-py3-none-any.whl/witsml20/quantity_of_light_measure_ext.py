from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.quantity_of_light_uom import QuantityOfLightUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class QuantityOfLightMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[QuantityOfLightUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
