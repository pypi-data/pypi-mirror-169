from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.linear_thermal_expansion_uom import LinearThermalExpansionUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LinearThermalExpansionMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[LinearThermalExpansionUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
