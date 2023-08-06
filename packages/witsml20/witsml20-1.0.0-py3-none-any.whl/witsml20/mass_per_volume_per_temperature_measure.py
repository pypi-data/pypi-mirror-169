from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.mass_per_volume_per_temperature_uom import MassPerVolumePerTemperatureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerVolumePerTemperatureMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MassPerVolumePerTemperatureUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
