from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.isothermal_compressibility_uom import IsothermalCompressibilityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IsothermalCompressibilityMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[IsothermalCompressibilityUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
