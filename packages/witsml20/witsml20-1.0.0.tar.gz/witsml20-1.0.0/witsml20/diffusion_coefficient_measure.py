from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.diffusion_coefficient_uom import DiffusionCoefficientUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DiffusionCoefficientMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[DiffusionCoefficientUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
