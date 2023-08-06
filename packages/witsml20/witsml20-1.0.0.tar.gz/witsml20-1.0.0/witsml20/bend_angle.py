from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_rotary_steerable_tool import AbstractRotarySteerableTool
from witsml20.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BendAngle(AbstractRotarySteerableTool):
    """
    Used with point-the-bit type of rotary steerable system tools; describes
    the angle of the bit.

    :ivar bend_angle: The angle of the bend.
    """
    bend_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "BendAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
