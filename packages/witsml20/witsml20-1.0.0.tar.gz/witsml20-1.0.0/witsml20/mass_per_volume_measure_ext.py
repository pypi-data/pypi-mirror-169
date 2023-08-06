from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.mass_per_volume_uom import MassPerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerVolumeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MassPerVolumeUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
