from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.cement_job_design import CementJobDesign
from witsml20.cement_job_report import CementJobReport
from witsml20.cement_job_type import CementJobType
from witsml20.cementing_fluid import CementingFluid
from witsml20.data_object_reference import DataObjectReference
from witsml20.length_measure import LengthMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CementJob(AbstractObject):
    """
    Used to capture information about cementing operations, which are done to
    seal the annulus after a casing string has been run, to seal a lost
    circulation zone, or to set a plug to support directional drilling
    operations or seal a well so that it may be abandoned.

    :ivar job_type: Type of cement job.
    :ivar job_config: Job configuration.
    :ivar name_cemented_string: Name for the cemented string
    :ivar name_work_string: Name for the cement work string
    :ivar offshore_job: Offshore job? Values are "true" (or "1") and
        "false" (or "0").
    :ivar md_water: Water depth if offshore. The distance from mean sea
        level to water bottom (seabed floor).
    :ivar returns_to_seabed: Returns to seabed? Values are "true" (or
        "1") and "false" (or "0").
    :ivar md_prev_shoe: Measured depth of previous shoe.
    :ivar md_hole: Measured depth at bottom of hole.
    :ivar tvd_prev_shoe: True vertical depth of previous shoe.
    :ivar md_string_set: Measured depth of cement string shoe.
    :ivar tvd_string_set: True vertical depth of cement string shoe.
    :ivar type_plug: Plug type.
    :ivar name_cement_string: Name for the cementing string
    :ivar type_squeeze: Type of squeeze.
    :ivar md_squeeze: Measured depth of squeeze.
    :ivar tool_company: Company providing the cementing tool.
    :ivar type_tool: Cement tool type.
    :ivar coil_tubing: Is coiled tubing used?  Values are "true" (or
        "1") and "false" (or "0").
    :ivar job_report:
    :ivar wellbore:
    :ivar hole_config:
    :ivar design:
    :ivar cementing_fluid:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    job_type: Optional[CementJobType] = field(
        default=None,
        metadata={
            "name": "JobType",
            "type": "Element",
        }
    )
    job_config: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobConfig",
            "type": "Element",
            "max_length": 2000,
        }
    )
    name_cemented_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameCementedString",
            "type": "Element",
            "max_length": 64,
        }
    )
    name_work_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameWorkString",
            "type": "Element",
            "max_length": 64,
        }
    )
    offshore_job: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OffshoreJob",
            "type": "Element",
        }
    )
    md_water: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MdWater",
            "type": "Element",
        }
    )
    returns_to_seabed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnsToSeabed",
            "type": "Element",
        }
    )
    md_prev_shoe: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdPrevShoe",
            "type": "Element",
        }
    )
    md_hole: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdHole",
            "type": "Element",
        }
    )
    tvd_prev_shoe: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "TvdPrevShoe",
            "type": "Element",
        }
    )
    md_string_set: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdStringSet",
            "type": "Element",
        }
    )
    tvd_string_set: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "TvdStringSet",
            "type": "Element",
        }
    )
    type_plug: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypePlug",
            "type": "Element",
            "max_length": 64,
        }
    )
    name_cement_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameCementString",
            "type": "Element",
            "max_length": 64,
        }
    )
    type_squeeze: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeSqueeze",
            "type": "Element",
            "max_length": 64,
        }
    )
    md_squeeze: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdSqueeze",
            "type": "Element",
        }
    )
    tool_company: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToolCompany",
            "type": "Element",
            "max_length": 64,
        }
    )
    type_tool: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeTool",
            "type": "Element",
            "max_length": 64,
        }
    )
    coil_tubing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CoilTubing",
            "type": "Element",
        }
    )
    job_report: Optional[CementJobReport] = field(
        default=None,
        metadata={
            "name": "JobReport",
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
    hole_config: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "HoleConfig",
            "type": "Element",
        }
    )
    design: Optional[CementJobDesign] = field(
        default=None,
        metadata={
            "name": "Design",
            "type": "Element",
        }
    )
    cementing_fluid: List[CementingFluid] = field(
        default_factory=list,
        metadata={
            "name": "CementingFluid",
            "type": "Element",
        }
    )
