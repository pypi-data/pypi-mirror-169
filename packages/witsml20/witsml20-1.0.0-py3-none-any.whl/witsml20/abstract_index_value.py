from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AbstractIndexValue:
    """Generic representation of pass, depth, or time values.

    Each derived element provides specialized implementation for
    specific content types or for optimization of the representation.
    """
