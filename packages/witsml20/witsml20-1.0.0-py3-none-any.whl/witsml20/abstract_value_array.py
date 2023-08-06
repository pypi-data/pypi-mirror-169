from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractValueArray:
    """Generic representation of an array of numeric, Boolean, and string
    values.

    Each derived element provides specialized implementation for
    specific content types or for optimization of the representation.
    """
