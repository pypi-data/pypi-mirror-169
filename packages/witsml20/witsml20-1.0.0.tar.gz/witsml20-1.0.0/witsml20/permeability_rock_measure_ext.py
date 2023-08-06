from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.permeability_rock_uom import PermeabilityRockUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PermeabilityRockMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[PermeabilityRockUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
