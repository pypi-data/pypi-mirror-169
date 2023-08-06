from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.geochronological_unit import GeochronologicalUnit
from witsml20.lithostratigraphic_unit import LithostratigraphicUnit
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.plane_angle_measure import PlaneAngleMeasure
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreMarker(AbstractObject):
    """Used to capture information about a geologic formation that was
    encountered in a wellbore.

    This object is uniquely identified within the context of one
    wellbore object.

    :ivar chronostratigraphic_top: The name of a geochronology for this
        marker, with the "kind" attribute specifying the
        geochronological time span.
    :ivar lithostratigraphic_top: Specifies the unit of
        lithostratigraphy.
    :ivar md: Logged measured depth at the top of marker.
    :ivar tvd: Logged true vertical depth at top of marker.
    :ivar dip_angle: Angle of dip with respect to horizontal.
    :ivar dip_direction: Interpreted downdip direction.
    :ivar trajectory:
    :ivar wellbore:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    chronostratigraphic_top: Optional[GeochronologicalUnit] = field(
        default=None,
        metadata={
            "name": "ChronostratigraphicTop",
            "type": "Element",
        }
    )
    lithostratigraphic_top: Optional[LithostratigraphicUnit] = field(
        default=None,
        metadata={
            "name": "LithostratigraphicTop",
            "type": "Element",
        }
    )
    md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "required": True,
        }
    )
    tvd: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
        }
    )
    dip_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "DipAngle",
            "type": "Element",
        }
    )
    dip_direction: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "DipDirection",
            "type": "Element",
        }
    )
    trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
        }
    )
