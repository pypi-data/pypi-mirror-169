from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MeasureOrQuantity:
    """A measure with a UOM or a quantity (without a UOM).

    This should not be used except in situations where the underlying
    class of data is captured elsewhere, e.g., in a measure class.

    :ivar value:
    :ivar uom: A measure with a UOM or a quantity (without a UOM). This
        should not be used except in situations where the underlying
        class of data is captured elsewhere, e.g., in a measure class.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        }
    )
