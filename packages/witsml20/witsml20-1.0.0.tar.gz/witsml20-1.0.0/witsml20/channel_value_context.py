from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_log_data_context import AbstractLogDataContext
from witsml20.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ChannelValueContext(AbstractLogDataContext):
    """
    Describes the data for the log in terms of  the value of a given channel.

    :ivar channel_reference: The channel refers to another Energistics
        data object.
    :ivar data_value: A free-form format to specify the data value.
    """
    channel_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChannelReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    data_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
