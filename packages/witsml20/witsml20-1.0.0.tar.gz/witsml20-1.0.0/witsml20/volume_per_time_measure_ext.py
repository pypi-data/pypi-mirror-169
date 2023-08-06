from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.volume_per_time_uom import VolumePerTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerTimeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[VolumePerTimeUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
