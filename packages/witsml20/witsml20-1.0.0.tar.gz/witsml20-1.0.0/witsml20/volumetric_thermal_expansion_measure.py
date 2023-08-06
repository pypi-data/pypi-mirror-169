from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.volumetric_thermal_expansion_uom import VolumetricThermalExpansionUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumetricThermalExpansionMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumetricThermalExpansionUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
