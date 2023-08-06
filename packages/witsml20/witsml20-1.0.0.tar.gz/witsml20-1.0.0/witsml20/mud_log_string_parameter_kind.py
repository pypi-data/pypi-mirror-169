from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class MudLogStringParameterKind(Enum):
    """
    Specifies values for mud log parameters that are described by character
    strings.
    """
    BIT_PARAMETERS = "bit parameters"
    BIT_TYPE_COMMENT = "bit type comment"
    CASING_POINT_COMMENT = "casing point comment"
    CHROMATOGRAPH_COMMENT = "chromatograph comment"
    CIRCULATION_SYSTEM_COMMENT = "circulation system comment"
    CORE_INTERVAL_COMMENT = "core interval comment"
    DRILLING_DATA_COMMENT = "drilling data comment"
    GAS_PEAKS_COMMENT = "gas peaks comment"
    GAS_RATIO_COMMENT = "gas ratio comment"
    GENERAL_ENGINEERING_COMMENT = "general engineering comment"
    LITHLOG_COMMENT = "lithlog comment"
    LWD_COMMENT = "LWD comment"
    MARKER_OR_FORMATION_TOP_COMMENT = "marker or formation top comment"
    MIDNIGHT_DEPTH_DATE = "midnight depth date"
    MUD_CHECK_COMMENT = "mud check comment"
    MUD_DATA_COMMENT = "mud data comment"
    MUDLOG_COMMENT = "mudlog comment"
    PRESSURE_DATA_COMMENT = "pressure data comment"
    SHALE_DENSITY_COMMENT = "shale density comment"
    SHORT_TRIP_COMMENT = "short trip comment"
    SHOW_REPORT_COMMENT = "show report comment"
    SIDEWALL_CORE_COMMENT = "sidewall core comment"
    SLIDING_INTERVAL = "sliding Interval"
    STEAM_STILL_RESULTS_COMMENT = "steam still results comment"
    SURVEY_COMMENT = "survey comment"
    TEMPERATURE_DATA_COMMENT = "temperature data comment"
    TEMPERATURE_TREND_COMMENT = "temperature trend comment"
    UNKNOWN = "unknown"
    WIRELINE_LOG_COMMENT = "wireline log comment"
