from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.length_per_mass_uom import LengthPerMassUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LengthPerMassMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LengthPerMassUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
