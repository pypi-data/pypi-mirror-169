from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.light_exposure_uom import LightExposureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LightExposureMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LightExposureUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
