from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_projected_crs import AbstractProjectedCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedEpsgCrs(AbstractProjectedCrs):
    """
    This class contains the EPSG code for a projected CRS.
    """
    epsg_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "EpsgCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
