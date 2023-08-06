from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.volume_uom import VolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
