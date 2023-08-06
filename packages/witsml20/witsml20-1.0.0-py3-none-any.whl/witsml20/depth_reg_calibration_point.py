from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.calibration_point_role import CalibrationPointRole
from witsml20.depth_reg_parameter import DepthRegParameter
from witsml20.depth_reg_point import DepthRegPoint
from witsml20.dimensionless_measure import DimensionlessMeasure
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.generic_measure import GenericMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthRegCalibrationPoint:
    """A mapping of pixel positions on the log image to rectified or depth-
    registered positions on the log image.

    Specifically, pixels along the depth track are tagged with the
    matching measured depth for that position.

    :ivar index: The index (depth or time) for the calibration point.
        The UOM value must be consistent with the indexType.
    :ivar track: A pointer to the track containing the point.
    :ivar role: The horizontal position on the grid that the calibration
        point represents.
    :ivar curve_name: Facilitates searching for logs based on curve
        type.
    :ivar fraction: An intermediate point from the left edge to the
        right edge. Required when CalibrationPointRole is "fraction";
        otherwise, not allowed otherwise.) Used to extrapolate the
        rectified position of a track boundary that has wandered off the
        edge of the image.
    :ivar comment: Comments about the log section.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar parameter:
    :ivar point:
    :ivar uid: Unique identifier for the calibration point.
    """
    index: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    track: Optional[str] = field(
        default=None,
        metadata={
            "name": "Track",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    role: Optional[CalibrationPointRole] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    curve_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurveName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    fraction: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "Fraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comment: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Comment",
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
    parameter: List[DepthRegParameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    point: Optional[DepthRegPoint] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
