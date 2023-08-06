from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_well_location import AbstractWellLocation
from witsml20.angle_per_length_measure import AnglePerLengthMeasure
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.plane_angle_measure import PlaneAngleMeasure
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportSurveyStation:
    """
    Trajectory station information for the drill report period.

    :ivar dtim: The date at which the directional survey took place.
    :ivar md: Measured depth of measurement from the drill datum.
    :ivar tvd: True vertical depth of the measurements.
    :ivar incl: Hole inclination, measured from vertical.
    :ivar azi: Hole azimuth, corrected to a well's azimuth reference.
    :ivar vert_sect: Distance along the vertical section of an azimuth
        plane.
    :ivar dls: Dogleg severity.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar location:
    :ivar uid: Unique identifier for this instance of
        DrillReportSurveyStation.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    tvd: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    incl: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Incl",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    azi: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Azi",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vert_sect: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "VertSect",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dls: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "Dls",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    location: List[AbstractWellLocation] = field(
        default_factory=list,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
