from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.force_uom import ForceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ForceMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ForceUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
