from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_bottom_hole_temperature import AbstractBottomHoleTemperature
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.md_interval import MdInterval
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.tvd_interval import TvdInterval
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportLogInfo:
    """
    General information about a log conducted during the drill report period.

    :ivar dtim: The date and time that the log was completed.
    :ivar run_number: Log run number. For measurement while drilling,
        this should be the bottom hole assembly number.
    :ivar service_company: Name of the contractor who provided the
        service.
    :ivar logged_md_interval: Measured depth interval from the top to
        the base of the interval logged.
    :ivar logged_tvd_interval: True vertical depth interval from the top
        to the base of the interval logged.
    :ivar tool: A description of the logging tool.
    :ivar md_temp_tool: Measured depth to the temperature measurement
        tool.
    :ivar tvd_temp_tool: True vertical depth to the temperature
        measurement tool.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar bottom_hole_temperature:
    :ivar uid: Unique identifier for this instance of
        DrillReportLogInfo.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    run_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RunNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    service_company: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceCompany",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    logged_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "LoggedMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    logged_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "LoggedTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tool: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    md_temp_tool: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdTempTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_temp_tool: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "TvdTempTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bottom_hole_temperature: Optional[AbstractBottomHoleTemperature] = field(
        default=None,
        metadata={
            "name": "BottomHoleTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
