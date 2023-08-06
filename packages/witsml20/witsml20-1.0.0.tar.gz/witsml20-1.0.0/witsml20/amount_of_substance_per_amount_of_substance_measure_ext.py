from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.amount_of_substance_per_amount_of_substance_uom import AmountOfSubstancePerAmountOfSubstanceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AmountOfSubstancePerAmountOfSubstanceMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[AmountOfSubstancePerAmountOfSubstanceUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
