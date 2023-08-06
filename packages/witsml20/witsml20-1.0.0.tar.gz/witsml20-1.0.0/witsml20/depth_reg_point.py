from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthRegPoint:
    """
    The position of a pixel of an image, in x-y coordinates.

    :ivar x: The x pixel position of a point.
    :ivar y: The y pixel position of a point.
    """
    x: Optional[int] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
