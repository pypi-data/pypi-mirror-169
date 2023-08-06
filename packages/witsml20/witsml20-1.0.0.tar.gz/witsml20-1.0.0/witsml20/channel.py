from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml20.abstract_index_value import AbstractIndexValue
from witsml20.abstract_object import AbstractObject
from witsml20.channel_derivation import ChannelDerivation
from witsml20.channel_index import ChannelIndex
from witsml20.channel_state import ChannelState
from witsml20.channel_status import ChannelStatus
from witsml20.data_object_reference import DataObjectReference
from witsml20.etp_data_type import EtpDataType
from witsml20.length_measure_ext import LengthMeasureExt
from witsml20.log_channel_axis import LogChannelAxis
from witsml20.logging_method import LoggingMethod
from witsml20.point_metadata import PointMetadata
from witsml20.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Channel(AbstractObject):
    """A channel object.

    It corresponds roughly to the LogCurveInfo structure in WITSML1411,
    and directly corresponds to the ChannelMetadataRecord structure in
    ETP. In historian terminology, a channel corresponds directly to a
    tag. Channels are the fundamental unit of organization for WITSML
    logs.

    :ivar mnemonic: The mnemonic name for this channel. Mnemonics are
        not unique within a store.
    :ivar data_type: The underlying ETP data type of the value.
    :ivar uom: The underlying unit of measure of the value.
    :ivar growing_status: The status of a channel with respect to
        creating new measurements. Statuses include: Active: A channel
        is actively producing data points. Inactive: A channel is
        offline or not currently producing, but may begin producing
        again in the future. Closed: A channel will never produce points
        again. The rules for when a channel is to be closed will vary
        some for different kinds of channels. For example, time-based
        surface channels may remain open for the entire life of the
        drilling operation, whereas depth-based wireline channels are
        closed at the end of the wireline job
    :ivar source: Source of the data in the channel. Enter the
        contractor name who conducted the log.
    :ivar wellbore:
    :ivar axis_definition:
    :ivar channel_state: Defines where the channel gets its data from,
        e.g., calculated from another source, or from archive, or raw
        real-time, etc.
    :ivar time_depth: Is this a time or depth log?
    :ivar channel_class: A mandatory value categorizing a log channel.
        The classification system used in WITSML is the one from the
        PWLS group. NOTE: This should turn into an extensible
        enumeration before WITSML is released.
    :ivar run_number: The nominal run number for the channel. No precise
        meaning is declared for this attribute but it is so commonly
        used that it must be included. The value here should match a bit
        run number for LWD data and a wireline run number for logging
        data.
    :ivar pass_number: The nominal pass number for the channel. No
        precise meaning is declared for this attribute but it is so
        commonly used that it must be included. The value here should
        match a wireline pass number for logging data.
    :ivar start_index: When the log header defines the direction as
        "Increasing", the startIndex is the starting (minimum) index
        value at which the first non-null data point is located. When
        the log header defines the direction as "Decreasing", the
        startIndex is the starting (maximum) index value at which the
        first non-null data point is located.
    :ivar end_index: When the log header defines the direction as
        "Increasing", the endIndex is the ending (maximum) index value
        at which the last non-null data point is located. When the log
        header defines the direction as Decreasing, the endIndex is the
        ending (minimum) index value at which the last non-null data
        point is located.
    :ivar logging_company_name: Name of the logging company.
    :ivar logging_company_code: The RP66 organization code assigned to a
        logging company. The list is available at
        http://www.energistics.org/geosciences/geology-
        standards/rp66-organization-codes
    :ivar tool_name: Name of the logging tool as given by the logging
        contractor.
    :ivar tool_class: A value categorizing a logging tool. The
        classification system used in WITSML is the one from the PWLS
        group. NOTE: This should turn into an extensible enumeration
        before WITSML is released
    :ivar derivation: Indicates that the channel is derived from one or
        more other channels
    :ivar logging_method: Defines where the log channel gets its data
        from: LWD, MWD, wireline; or whether it is computed, etc.
    :ivar nominal_hole_size: The nominal hole size at the time the
        measurement tool was in the hole. The size is "nominal" to
        indicate that this is not the result of a caliper reading or
        other direct measurement of the hoe size, but is just a name
        used to refer to the diameter. This is normally the bit size. In
        a case where there are more than one diameter hole being drilled
        at the same time (like where a reamer is behind the bit) this
        diameter is the one which was seen by the sensor which produced
        a particular log channel.
    :ivar point_metadata:
    :ivar derived_from:
    :ivar index:
    :ivar parent:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    mnemonic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mnemonic",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    data_type: Optional[EtpDataType] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Element",
            "required": True,
        }
    )
    uom: Optional[Union[UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    growing_status: Optional[ChannelStatus] = field(
        default=None,
        metadata={
            "name": "GrowingStatus",
            "type": "Element",
            "required": True,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "max_length": 64,
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
        }
    )
    axis_definition: List[LogChannelAxis] = field(
        default_factory=list,
        metadata={
            "name": "AxisDefinition",
            "type": "Element",
        }
    )
    channel_state: Optional[ChannelState] = field(
        default=None,
        metadata={
            "name": "ChannelState",
            "type": "Element",
        }
    )
    time_depth: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeDepth",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    channel_class: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChannelClass",
            "type": "Element",
            "required": True,
        }
    )
    run_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RunNumber",
            "type": "Element",
            "max_length": 64,
        }
    )
    pass_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassNumber",
            "type": "Element",
            "max_length": 64,
        }
    )
    start_index: Optional[AbstractIndexValue] = field(
        default=None,
        metadata={
            "name": "StartIndex",
            "type": "Element",
        }
    )
    end_index: Optional[AbstractIndexValue] = field(
        default=None,
        metadata={
            "name": "EndIndex",
            "type": "Element",
        }
    )
    logging_company_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoggingCompanyName",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    logging_company_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoggingCompanyCode",
            "type": "Element",
            "max_length": 64,
        }
    )
    tool_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToolName",
            "type": "Element",
            "max_length": 64,
        }
    )
    tool_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToolClass",
            "type": "Element",
            "max_length": 64,
        }
    )
    derivation: Optional[ChannelDerivation] = field(
        default=None,
        metadata={
            "name": "Derivation",
            "type": "Element",
        }
    )
    logging_method: Optional[LoggingMethod] = field(
        default=None,
        metadata={
            "name": "LoggingMethod",
            "type": "Element",
        }
    )
    nominal_hole_size: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "NominalHoleSize",
            "type": "Element",
        }
    )
    point_metadata: List[PointMetadata] = field(
        default_factory=list,
        metadata={
            "name": "PointMetadata",
            "type": "Element",
        }
    )
    derived_from: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "DerivedFrom",
            "type": "Element",
        }
    )
    index: List[ChannelIndex] = field(
        default_factory=list,
        metadata={
            "name": "Index",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    parent: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
        }
    )
