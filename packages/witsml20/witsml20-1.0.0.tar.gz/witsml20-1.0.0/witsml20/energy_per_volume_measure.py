from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.energy_per_volume_uom import EnergyPerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class EnergyPerVolumeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[EnergyPerVolumeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
