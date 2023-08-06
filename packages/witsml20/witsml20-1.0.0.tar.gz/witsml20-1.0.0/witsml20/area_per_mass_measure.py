from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.area_per_mass_uom import AreaPerMassUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AreaPerMassMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AreaPerMassUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
