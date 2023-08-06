from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.depth_reg_rectangle import DepthRegRectangle
from witsml20.depth_reg_track_curve import DepthRegTrackCurve
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.log_track_type import LogTrackType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthRegTrack:
    """
    Horizontal track layout of the rectified log image that identifies the
    rectangle for a single log track.

    :ivar name: A label associated with the track.
    :ivar type: The kind of track.
    :ivar left_edge: The position of the left edge of the track.
    :ivar right_edge: The position of the right edge of the track.
    :ivar track_curve_scale_rect: Coordinates of rectangle representing
        the track.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar associated_curve:
    :ivar uid: Unique identifier for the track.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    type: Optional[LogTrackType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    left_edge: Optional[int] = field(
        default=None,
        metadata={
            "name": "LeftEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    right_edge: Optional[int] = field(
        default=None,
        metadata={
            "name": "RightEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    track_curve_scale_rect: List[DepthRegRectangle] = field(
        default_factory=list,
        metadata={
            "name": "TrackCurveScaleRect",
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
    associated_curve: List[DepthRegTrackCurve] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedCurve",
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
