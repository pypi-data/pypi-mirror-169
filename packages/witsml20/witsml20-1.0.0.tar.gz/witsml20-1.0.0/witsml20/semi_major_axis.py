from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SemiMajorAxis:
    """gml:semiMajorAxis specifies the length of the semi-major axis of the
    ellipsoid, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a length, such as metres or
    feet.
    """
    class Meta:
        name = "semiMajorAxis"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
