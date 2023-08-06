from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.channel_status import ChannelStatus
from witsml20.data_object_reference import DataObjectReference
from witsml20.interpreted_geology_interval import InterpretedGeologyInterval
from witsml20.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class InterpretedGeology(AbstractObject):
    """A container object for zero or more InterpretedGeologyInterval objects.

    The container references a specific wellbore, a depth interval, a
    growing object status, and a collection of interpreted geology
    intervals. These values are manually entered per sample by the
    wellsite geologist or mud logger as an interpretation of the actual
    lithology sequence along the length of the wellbore by correlating
    the percentage lithologies observed in the cuttings samples along
    with other data (typically the drill rate and gamma ray curves), to
    estimate the location of the boundaries between the different
    lithology types. This analysis creates a sequence of individual
    lithologies along the wellbore. Therefore, InterpretedGeology
    typically contains a single lithology element for each interval that
    captures the detailed geological description of the lithology.

    :ivar md_interval: [maintained by the server] The interval that
        contains the minimum and maximum measured depths for all
        interpreted intervals in this interpreted geology.
    :ivar growing_status: Describes the growing status of the
        interpreted geology. Valid values: active, inactive or closed.
    :ivar geologic_interval_interpreted:
    :ivar wellbore:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "required": True,
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
    geologic_interval_interpreted: List[InterpretedGeologyInterval] = field(
        default_factory=list,
        metadata={
            "name": "GeologicIntervalInterpreted",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
