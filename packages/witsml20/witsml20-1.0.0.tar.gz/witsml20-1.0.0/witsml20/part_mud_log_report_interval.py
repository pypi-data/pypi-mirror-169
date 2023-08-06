from __future__ import annotations
from dataclasses import dataclass
from witsml20.mudlog_report_interval import MudlogReportInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PartMudLogReportInterval(MudlogReportInterval):
    """
    Wrapper for sending individual MudLogReportIntervals using ETP.
    """
    class Meta:
        name = "part_MudLogReportInterval"
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"
