from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_well_location import AbstractWellLocation
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.well_elevation_coord import WellElevationCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ReferencePoint:
    """
    Reference Point Component Schema.

    :ivar name: Human-recognizable context for the point.
    :ivar type: The kind of point. For example, 'well reference point',
        'platform reference point', 'sea surface', 'sea bottom'.
    :ivar measured_depth: The measured depth coordinate of this
        reference point. Value is positive when moving toward the
        bottomhole from the measured depth datum. Provide a value for
        this when the reference is "downhole", such as an ocean-bottom
        template, or when the reference point is also used as a vertical
        well datum. The measured depth value can be used to determine if
        the reference pointand a vertical well datum are at the same
        point.
    :ivar description: A textual description of the point.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar elevation:
    :ivar location:
    :ivar uid: A unique identifier for an instance of a ReferencePoint.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    measured_depth: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MeasuredDepth",
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
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    elevation: Optional[WellElevationCoord] = field(
        default=None,
        metadata={
            "name": "Elevation",
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
            "min_occurs": 1,
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
