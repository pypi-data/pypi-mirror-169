from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.channel_status import ChannelStatus
from witsml20.cuttings_geology_interval import CuttingsGeologyInterval
from witsml20.data_object_reference import DataObjectReference
from witsml20.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CuttingsGeology(AbstractObject):
    """Container for Cuttings Lithology items.

    The mud logger at the wellsite takes regular samples of drilled
    cuttings while the well is being drilled and examines the cuttings
    to determine the rock types (lithologies) present in each sample.
    The cuttings samples will typically contain a mix of different
    lithologies in each sample because there may have been multiple rock
    types that were drilled within the sample depth interval and there
    can also be mixing of cuttings as they travel up the wellbore and
    are collected on the shakers. CuttingsGeology therefore will
    typically contain multiple lithology elements for each interval so
    that the percentages of each lithology in the sample along with the
    more detailed geological description can be recorded.

    :ivar md_interval: [maintained by the server] The interval which
        contains the minimum and maximum measured depths for all
        cuttings intervals in this cuttings geology.
    :ivar growing_status: Describes the growing status of the cuttings,
        whether active, inactive or closed
    :ivar cuttings_interval:
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
    cuttings_interval: List[CuttingsGeologyInterval] = field(
        default_factory=list,
        metadata={
            "name": "CuttingsInterval",
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
