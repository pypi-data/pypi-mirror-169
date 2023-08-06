from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.potential_difference_per_power_drop_uom import PotentialDifferencePerPowerDropUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PotentialDifferencePerPowerDropMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PotentialDifferencePerPowerDropUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
