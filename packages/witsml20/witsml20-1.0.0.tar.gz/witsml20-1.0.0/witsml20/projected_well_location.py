from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_projected_crs import AbstractProjectedCrs
from witsml20.abstract_well_location import AbstractWellLocation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ProjectedWellLocation(AbstractWellLocation):
    """
    Projected location of the well.

    :ivar coordinate1: The first coordinate based on a projected
        coordinate reference system.
    :ivar coordinate2: The second coordinate based on a projected
        coordinate reference system.
    :ivar crs:
    """
    coordinate1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    coordinate2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    crs: Optional[AbstractProjectedCrs] = field(
        default=None,
        metadata={
            "name": "Crs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
