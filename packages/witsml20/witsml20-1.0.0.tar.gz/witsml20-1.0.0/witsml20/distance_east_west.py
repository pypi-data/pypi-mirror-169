from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.east_or_west import EastOrWest
from witsml20.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DistanceEastWest:
    """The distance to a one-minute boundary on the east or west of a point.

    USA Public Land Survey System.

    :ivar value:
    :ivar uom: The unit of measure of the east-west distance.
    :ivar reference: East or west direction.
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
    reference: Optional[EastOrWest] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
