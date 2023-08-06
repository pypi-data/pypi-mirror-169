from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.channel_status import ChannelStatus
from witsml20.data_object_reference import DataObjectReference
from witsml20.md_interval import MdInterval
from witsml20.mud_log_parameter import MudLogParameter
from witsml20.mudlog_report_interval import MudlogReportInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudLogReport(AbstractObject):
    """
    Details of wellbore geology intervals, drilling parameters, chromatograph,
    mud gas, etc., data within an MD interval.

    :ivar mud_log_company: Name of the company recording the
        information.
    :ivar mud_log_engineers: Concatenated names of the mudloggers
        constructing the log.
    :ivar mud_log_geologists: Concatenated names of the geologists
        constructing the log.
    :ivar report_md_interval: [maintained by the server] The interval
        between the minimum and maximum measured depths contained in
        this MudLog report.
    :ivar growing_status: The growing state of the mudlog,. Valid
        Values: active, inactive or closed.
    :ivar wellbore:
    :ivar wellbore_geology:
    :ivar mudlog_intervals:
    :ivar related_logs:
    :ivar parameter:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    mud_log_company: Optional[str] = field(
        default=None,
        metadata={
            "name": "MudLogCompany",
            "type": "Element",
            "max_length": 64,
        }
    )
    mud_log_engineers: Optional[str] = field(
        default=None,
        metadata={
            "name": "MudLogEngineers",
            "type": "Element",
            "max_length": 2000,
        }
    )
    mud_log_geologists: Optional[str] = field(
        default=None,
        metadata={
            "name": "MudLogGeologists",
            "type": "Element",
            "max_length": 2000,
        }
    )
    report_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "ReportMdInterval",
            "type": "Element",
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
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
    wellbore_geology: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WellboreGeology",
            "type": "Element",
        }
    )
    mudlog_intervals: List[MudlogReportInterval] = field(
        default_factory=list,
        metadata={
            "name": "MudlogIntervals",
            "type": "Element",
        }
    )
    related_logs: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "RelatedLogs",
            "type": "Element",
        }
    )
    parameter: List[MudLogParameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
        }
    )
