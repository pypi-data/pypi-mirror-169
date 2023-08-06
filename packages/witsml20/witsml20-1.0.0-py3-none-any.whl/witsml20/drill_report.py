from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.bit_record import BitRecord
from witsml20.data_object_reference import DataObjectReference
from witsml20.drill_activity import DrillActivity
from witsml20.drill_report_control_incident_info import DrillReportControlIncidentInfo
from witsml20.drill_report_core_info import DrillReportCoreInfo
from witsml20.drill_report_equip_failure_info import DrillReportEquipFailureInfo
from witsml20.drill_report_form_test_info import DrillReportFormTestInfo
from witsml20.drill_report_gas_reading_info import DrillReportGasReadingInfo
from witsml20.drill_report_lith_show_info import DrillReportLithShowInfo
from witsml20.drill_report_log_info import DrillReportLogInfo
from witsml20.drill_report_perf_info import DrillReportPerfInfo
from witsml20.drill_report_pore_pressure import DrillReportPorePressure
from witsml20.drill_report_status_info import DrillReportStatusInfo
from witsml20.drill_report_strat_info import DrillReportStratInfo
from witsml20.drill_report_survey_station import DrillReportSurveyStation
from witsml20.drill_report_well_test_info import DrillReportWellTestInfo
from witsml20.drill_report_wellbore_info import DrillReportWellboreInfo
from witsml20.fluid import Fluid
from witsml20.object_alias import ObjectAlias
from witsml20.ops_report_version import OpsReportVersion
from witsml20.timestamped_comment_string import TimestampedCommentString
from witsml20.well_datum import WellDatum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReport(AbstractObject):
    """Used to capture a daily drilling report focused on reporting from the
    operator to partners or to a governmental agency.

    For a similar report whose focus is service company to operator, see
    the OpsReport object.

    :ivar dtim_start: Date and time that the reporting period started. A
        report period is commonly 24 hours.
    :ivar dtim_end: Date and time that the reporting period ended. A
        report period is commonly 24 hours.
    :ivar version_kind: The kind of report version. For example, a
        preliminary version.
    :ivar create_date: The date and time the report was created. A later
        timestamp indicates a newer version of the report. To update
        values in a report, a full updated copy of the original report
        should be submitted.
    :ivar well_datum: Defines a vertical datum used for measured depths,
        vertical depths, or elevations. If one of these coordinate
        values is included in the report, then you must specify a well
        datum. This requirement only applies to this report, which is
        generally a copy of the same information from the well object.
    :ivar bit_record: Information about a bit.
    :ivar drill_activity:
    :ivar log_info:
    :ivar core_info:
    :ivar well_test_info:
    :ivar form_test_info:
    :ivar lith_show_info:
    :ivar equip_failure_info:
    :ivar control_incident_info:
    :ivar strat_info:
    :ivar perf_info:
    :ivar gas_reading_info:
    :ivar wellbore:
    :ivar well_alias:
    :ivar wellbore_alias:
    :ivar wellbore_info:
    :ivar status_info:
    :ivar fluid:
    :ivar pore_pressure:
    :ivar extended_report:
    :ivar survey_station:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    version_kind: Optional[OpsReportVersion] = field(
        default=None,
        metadata={
            "name": "VersionKind",
            "type": "Element",
        }
    )
    create_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    well_datum: List[WellDatum] = field(
        default_factory=list,
        metadata={
            "name": "WellDatum",
            "type": "Element",
        }
    )
    bit_record: List[BitRecord] = field(
        default_factory=list,
        metadata={
            "name": "BitRecord",
            "type": "Element",
        }
    )
    drill_activity: List[DrillActivity] = field(
        default_factory=list,
        metadata={
            "name": "DrillActivity",
            "type": "Element",
        }
    )
    log_info: List[DrillReportLogInfo] = field(
        default_factory=list,
        metadata={
            "name": "LogInfo",
            "type": "Element",
        }
    )
    core_info: List[DrillReportCoreInfo] = field(
        default_factory=list,
        metadata={
            "name": "CoreInfo",
            "type": "Element",
        }
    )
    well_test_info: List[DrillReportWellTestInfo] = field(
        default_factory=list,
        metadata={
            "name": "WellTestInfo",
            "type": "Element",
        }
    )
    form_test_info: List[DrillReportFormTestInfo] = field(
        default_factory=list,
        metadata={
            "name": "FormTestInfo",
            "type": "Element",
        }
    )
    lith_show_info: List[DrillReportLithShowInfo] = field(
        default_factory=list,
        metadata={
            "name": "LithShowInfo",
            "type": "Element",
        }
    )
    equip_failure_info: List[DrillReportEquipFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "EquipFailureInfo",
            "type": "Element",
        }
    )
    control_incident_info: List[DrillReportControlIncidentInfo] = field(
        default_factory=list,
        metadata={
            "name": "ControlIncidentInfo",
            "type": "Element",
        }
    )
    strat_info: List[DrillReportStratInfo] = field(
        default_factory=list,
        metadata={
            "name": "StratInfo",
            "type": "Element",
        }
    )
    perf_info: List[DrillReportPerfInfo] = field(
        default_factory=list,
        metadata={
            "name": "PerfInfo",
            "type": "Element",
        }
    )
    gas_reading_info: List[DrillReportGasReadingInfo] = field(
        default_factory=list,
        metadata={
            "name": "GasReadingInfo",
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
    well_alias: Optional[ObjectAlias] = field(
        default=None,
        metadata={
            "name": "WellAlias",
            "type": "Element",
        }
    )
    wellbore_alias: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "WellboreAlias",
            "type": "Element",
        }
    )
    wellbore_info: Optional[DrillReportWellboreInfo] = field(
        default=None,
        metadata={
            "name": "WellboreInfo",
            "type": "Element",
        }
    )
    status_info: List[DrillReportStatusInfo] = field(
        default_factory=list,
        metadata={
            "name": "StatusInfo",
            "type": "Element",
        }
    )
    fluid: List[Fluid] = field(
        default_factory=list,
        metadata={
            "name": "Fluid",
            "type": "Element",
        }
    )
    pore_pressure: List[DrillReportPorePressure] = field(
        default_factory=list,
        metadata={
            "name": "PorePressure",
            "type": "Element",
        }
    )
    extended_report: Optional[TimestampedCommentString] = field(
        default=None,
        metadata={
            "name": "ExtendedReport",
            "type": "Element",
        }
    )
    survey_station: List[DrillReportSurveyStation] = field(
        default_factory=list,
        metadata={
            "name": "SurveyStation",
            "type": "Element",
        }
    )
