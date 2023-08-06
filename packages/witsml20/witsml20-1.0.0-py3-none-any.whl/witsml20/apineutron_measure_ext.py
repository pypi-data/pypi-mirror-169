from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.apineutron_uom import ApineutronUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ApineutronMeasureExt:
    class Meta:
        name = "APINeutronMeasureExt"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ApineutronUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
