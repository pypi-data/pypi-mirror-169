from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.permeability_length_uom import PermeabilityLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PermeabilityLengthMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[PermeabilityLengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
