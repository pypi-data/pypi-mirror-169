from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.channel_index_type import ChannelIndexType
from witsml20.index_direction import IndexDirection
from witsml20.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ChannelIndex:
    """
    A read-only class that is the union of those channel indexes that are
    shared by all channels in the channel set.

    :ivar index_type: The type of index (time, depth, etc.).
    :ivar uom: The unit of measure of the index. Must be one of the
        units allowed for the specified IndexType (i.e., time or
        distance).
    :ivar direction: The direction of the index, either increasing or
        decreasing. Index direction may not change within the life of a
        channel.
    :ivar mnemonic: The mnemonic for the index.
    :ivar datum_reference: For depth indexes, this contains the UID of
        the datum, in a channel's Well object, to which all of the index
        values are referenced.
    """
    index_type: Optional[ChannelIndexType] = field(
        default=None,
        metadata={
            "name": "IndexType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    uom: Optional[Union[UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    direction: Optional[IndexDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    mnemonic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mnemonic",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    datum_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatumReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
