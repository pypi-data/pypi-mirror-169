from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.md_interval import MdInterval
from witsml20.perforation_status import PerforationStatus
from witsml20.tvd_interval import TvdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PerforationStatusHistory:
    """
    Information on the collection of perforation status history.

    :ivar perforation_status: Perforation status.
    :ivar start_date: The start date of the status.
    :ivar end_date: The end date of the status.
    :ivar perforation_md_interval: Overall measured depth interval for
        this perforated interval.
    :ivar perforation_tvd_interval: Overall true vertical depth interval
        for this perforated interval.
    :ivar allocation_factor: Defines the proportional amount of fluid
        from the well completion that is flowing through this interval
        within a wellbore.
    :ivar comment: Remarks and comments about the status.
    :ivar uid: Unique identifier for this instance of
        PerforationStatusHistory.
    """
    perforation_status: Optional[PerforationStatus] = field(
        default=None,
        metadata={
            "name": "PerforationStatus",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    perforation_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "PerforationMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "PerforationTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    allocation_factor: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllocationFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
