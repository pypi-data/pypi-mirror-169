from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellVerticalDepthCoord:
    """A vertical (gravity-based) depth coordinate within the context of a
    well.

    Positive moving downward from the reference datum. All coordinates
    with the same datum (and same UOM) can be considered to be in the
    same coordinate reference system (CRS) and are thus directly
    comparable.

    :ivar value:
    :ivar uom: Unit of measure used by this vertical depth coordinate
    :ivar datum: Defines the vertical datums associated with elevation,
        vertical depth and measured depth coordinates
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
    datum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
