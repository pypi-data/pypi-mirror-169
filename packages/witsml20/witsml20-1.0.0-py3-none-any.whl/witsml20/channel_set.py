from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_index_value import AbstractIndexValue
from witsml20.abstract_log_data_context import AbstractLogDataContext
from witsml20.abstract_object import AbstractObject
from witsml20.channel import Channel
from witsml20.channel_data import ChannelData
from witsml20.channel_derivation import ChannelDerivation
from witsml20.channel_index import ChannelIndex
from witsml20.channel_state import ChannelState
from witsml20.data_object_reference import DataObjectReference
from witsml20.length_measure_ext import LengthMeasureExt
from witsml20.logging_method import LoggingMethod

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ChannelSet(AbstractObject):
    """A grouping of channels with a compatible index, for some purpose.

    Each channel has its own index. A ‘compatible’ index simply means
    that all of the channels are either in time or in depth using a
    common datum.

    :ivar index:
    :ivar channel:
    :ivar data:
    :ivar channel_state: Defines where the channel gets its data from,
        e.g., calculated from another source, or from archive, or raw
        real-time, etc.
    :ivar time_depth: Use to indicate if this is a time or depth log.
    :ivar channel_class: A mandatory value categorizing a log channel.
        The classification system used in WITSML is the one from the
        PWLS group.
    :ivar run_number: The nominal run number for the channel. No precise
        meaning is declared for this attribute but it is so commonly
        used that it must be included. The value here should match a bit
        run number for LWD data and a wireline run number for logging
        data.
    :ivar pass_number: The nominal pass number for the channel. No
        precise meaning is declared for this attribute but it is so
        commonly used that it must be included. The value here should
        match a wireline pass number for logging data.
    :ivar start_index: When the log header defines the direction as: -
        "Increasing", the startIndex is the starting (minimum) index
        value at which the first non-null data point is located. -
        "Decreasing", the startIndex is the starting (maximum) index
        value at which the first non-null data point is located.
    :ivar end_index: When the log header defines the direction as: -
        "Increasing", the endIndex is the ending (maximum) index value
        at which the last non-null data point is located. -
        "Decreasing", the endIndex is the ending (minimum) index value
        at which the last non-null data point is located.
    :ivar logging_company_name: Name of the logging company.
    :ivar logging_company_code: The RP66 organization code assigned to a
        logging company. The list is available at
        http://www.energistics.org/geosciences/geology-
        standards/rp66-organization-codes
    :ivar tool_name: Name of the logging tool as given by the logging
        contractor.
    :ivar tool_class: A value categorizing a logging tool. The
        classification system used in WITSML is the one from the PWLS
        group.
    :ivar derivation: Indicates that the channel is derived from one or
        more other channels.
    :ivar logging_method: Defines where the log channel gets its data
        from: LWD, MWD, wireline; or whether it is computed, etc.
    :ivar nominal_hole_size: The nominal hole size (typically the bit
        size) at the time the measurement tool was in the hole. The size
        is "nominal" to indicate that this is not the result of a
        caliper reading or other direct measurement of the hole size,
        but is just a name used to refer to the diameter. When more than
        one diameter holes are being drilled at the same time (e.g.,
        where a reamer is behind the bit), this diameter is the one that
        was seen by the sensor that produced a particular log channel.
    :ivar wellbore:
    :ivar data_context:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    index: List[ChannelIndex] = field(
        default_factory=list,
        metadata={
            "name": "Index",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    channel: List[Channel] = field(
        default_factory=list,
        metadata={
            "name": "Channel",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    data: Optional[ChannelData] = field(
        default=None,
        metadata={
            "name": "Data",
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
            "max_length": 64,
        }
    )
    channel_class: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChannelClass",
            "type": "Element",
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
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
        }
    )
    data_context: Optional[AbstractLogDataContext] = field(
        default=None,
        metadata={
            "name": "DataContext",
            "type": "Element",
        }
    )
