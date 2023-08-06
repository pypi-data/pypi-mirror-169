from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_geodetic_crs import AbstractGeodeticCrs
from witsml20.abstract_well_location import AbstractWellLocation
from witsml20.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class GeodeticWellLocation(AbstractWellLocation):
    """
    Location of the well by latitude and longitude.

    :ivar latitude: The latitude with north being positive.
    :ivar longitude: The longitude with east being positive.
    :ivar crs:
    """
    latitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    longitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    crs: Optional[AbstractGeodeticCrs] = field(
        default=None,
        metadata={
            "name": "Crs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
