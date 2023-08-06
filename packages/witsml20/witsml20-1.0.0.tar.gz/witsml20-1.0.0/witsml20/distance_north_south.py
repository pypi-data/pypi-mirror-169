from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.length_uom import LengthUom
from witsml20.north_or_south import NorthOrSouth

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DistanceNorthSouth:
    """The distance to a one-minute boundary on the north or south of a point.

    USA Public Land Survey System

    :ivar value:
    :ivar uom: The unit of measure of the north-south distance.
    :ivar reference: North or south direction.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    reference: Optional[NorthOrSouth] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
