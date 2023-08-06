from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class LogChannelAxis:
    """Metadata by which the array structure of a compound value is defined.

    It defines one axis of an array type used in a log channel.

    :ivar axis_start: Value of the initial entry in the list of axis
        index values.
    :ivar axis_spacing: The increment to be used to fill out the list of
        the log channel axis index values.
    :ivar axis_count: The count of elements along this axis of the
        array.
    :ivar axis_name: The name of the array axis.
    :ivar axis_property_kind: The property type by which the array axis
        is classified. Like "measured depth" or "elapsed time".
    :ivar axis_uom: A string representing the units of measure of the
        axis values.
    :ivar uid: A unique identifier for an instance of a log channel axis
    """
    axis_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "AxisStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    axis_spacing: Optional[float] = field(
        default=None,
        metadata={
            "name": "AxisSpacing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    axis_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "AxisCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    axis_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AxisName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    axis_property_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "AxisPropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    axis_uom: Optional[Union[UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "AxisUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".*:.*",
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
