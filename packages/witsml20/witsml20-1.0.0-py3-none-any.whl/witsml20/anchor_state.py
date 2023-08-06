from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.force_measure import ForceMeasure
from witsml20.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AnchorState:
    """
    :ivar anchor_name: The anchor number within a mooring system, or
        name if a name is used instead.
    :ivar anchor_angle: Angle of the anchor or mooring line.
    :ivar anchor_tension: Tension on the mooring line represented by the
        named anchor.
    :ivar description: Free-test description of the state of this anchor
        or mooring line.
    """
    anchor_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnchorName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    anchor_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AnchorAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    anchor_tension: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "AnchorTension",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
