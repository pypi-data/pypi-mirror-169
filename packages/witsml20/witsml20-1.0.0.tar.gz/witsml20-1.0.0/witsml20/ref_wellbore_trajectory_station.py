from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RefWellboreTrajectoryStation:
    """A reference to a trajectoryStation in a wellbore.

    The trajectoryStation may be defined within the context of another
    wellbore. This value represents a foreign key from one element to
    another.

    :ivar station_reference: A pointer to the trajectoryStation within
        the parent trajectory. StationReference is a special case where
        WITSML only uses a UID for the pointer.The natural identity of a
        station is its physical characteristics (e.g., md).
    :ivar trajectory_parent: A pointer to the trajectory within the
        parent wellbore. This trajectory contains the trajectoryStation.
    :ivar wellbore_parent: A pointer to the wellbore that contains the
        trajectory. WellboreParent is not needed unless the trajectory
        is outside the context of a common parent wellbore.
    """
    station_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "StationReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    trajectory_parent: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrajectoryParent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    wellbore_parent: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellboreParent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
