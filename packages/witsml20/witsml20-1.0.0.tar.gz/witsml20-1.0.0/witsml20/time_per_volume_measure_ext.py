from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.time_per_volume_uom import TimePerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TimePerVolumeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[TimePerVolumeUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
