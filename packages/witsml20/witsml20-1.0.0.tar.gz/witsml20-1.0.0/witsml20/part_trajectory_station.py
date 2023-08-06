from __future__ import annotations
from dataclasses import dataclass
from witsml20.trajectory_station import TrajectoryStation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PartTrajectoryStation(TrajectoryStation):
    """
    Wrapper for sending individual stations using ETP.
    """
    class Meta:
        name = "part_TrajectoryStation"
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"
