from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_rotary_steerable_tool import AbstractRotarySteerableTool
from witsml20.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BendOffset(AbstractRotarySteerableTool):
    """
    Used with point-the-bit type of rotary steerable system tools; describes
    the angle of the bit.

    :ivar bend_offset: Offset distance from the bottom connection to the
        bend.
    """
    bend_offset: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BendOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
