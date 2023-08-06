from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.force_per_volume_measure import ForcePerVolumeMeasure
from witsml20.length_measure import LengthMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.pressure_measure import PressureMeasure
from witsml20.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CementJobEvaluation(AbstractObject):
    """
    A top-level object that is used to record the testing and evaluation of a
    previously performed cement job.

    :ivar pres_test: Test pressure.
    :ivar etim_test: Elapsed tome to perform the test.
    :ivar cement_shoe_collar: Cement found between shoe and collar?
        Values are "true" (or "1") and "false" (or "0").
    :ivar cet_run: Cement evaluation tool run?  Values are "true" (or
        "1") and "false" (or "0").
    :ivar cet_bond_qual: Cement evaluation tool bond quality?  Values
        are "true" (or "1") and "false" (or "0").
    :ivar cbl_run: Cement bond log run? Values are "true" (or "1") and
        "false" (or "0").
    :ivar cbl_bond_qual: Cement bond log quality indication?  Values are
        "true" (or "1") and "false" (or "0").
    :ivar cbl_pres: Cement bond log under pressure.
    :ivar temp_survey: Temperature survey run?  Values are "true" (or
        "1") and "false" (or "0").
    :ivar etim_cement_log: Hours before logging run after cement run.
    :ivar form_pit: Pressure integrity test/leak-off test formation
        breakdown gradient or absolute pressure.
    :ivar tool_company_pit: Tool name for the pressure integrity test.
    :ivar etim_pit_start: Hours between end of cement job and the start
        of the pressure integrity test.
    :ivar md_cement_top: Measured depth at top of cement.
    :ivar top_cement_method: Method to determine cement top.
    :ivar toc_ok: Is the top of cement sufficient?  Values are "true"
        (or "1") and "false" (or "0").
    :ivar job_rating: Job rating.
    :ivar remedial_cement: Remedial cement required?  Values are "true"
        (or "1") and "false" (or "0").
    :ivar num_remedial: Number of remedials.
    :ivar failure_method: Method used to determine that a cement job was
        unsuccessful.
    :ivar liner_top: The distance to the top of the liner.
    :ivar liner_lap: Liner overlap length.
    :ivar etim_before_test: Hours before the liner top test.
    :ivar test_negative_tool: Test negative tool used for the liner top
        seal.
    :ivar test_negative_emw: Equivalent mud weight. Negative test.
    :ivar test_positive_tool: Test positive tool for liner top seal.
    :ivar test_positive_emw: Equivalent mud weight. Positive test or
        absolute pressure .
    :ivar cement_found_on_tool: Cement found on tool?  Values are "true"
        (or "1") and "false" (or "0").
    :ivar md_dvtool: Measured depth to the diverter tool.
    :ivar cement_job:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    pres_test: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresTest",
            "type": "Element",
        }
    )
    etim_test: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimTest",
            "type": "Element",
        }
    )
    cement_shoe_collar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CementShoeCollar",
            "type": "Element",
        }
    )
    cet_run: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CetRun",
            "type": "Element",
        }
    )
    cet_bond_qual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CetBondQual",
            "type": "Element",
        }
    )
    cbl_run: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CblRun",
            "type": "Element",
        }
    )
    cbl_bond_qual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CblBondQual",
            "type": "Element",
        }
    )
    cbl_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "CblPres",
            "type": "Element",
        }
    )
    temp_survey: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempSurvey",
            "type": "Element",
        }
    )
    etim_cement_log: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimCementLog",
            "type": "Element",
        }
    )
    form_pit: Optional[ForcePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FormPit",
            "type": "Element",
        }
    )
    tool_company_pit: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToolCompanyPit",
            "type": "Element",
            "max_length": 64,
        }
    )
    etim_pit_start: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimPitStart",
            "type": "Element",
        }
    )
    md_cement_top: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdCementTop",
            "type": "Element",
        }
    )
    top_cement_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "TopCementMethod",
            "type": "Element",
            "max_length": 64,
        }
    )
    toc_ok: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TocOK",
            "type": "Element",
        }
    )
    job_rating: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobRating",
            "type": "Element",
            "max_length": 64,
        }
    )
    remedial_cement: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RemedialCement",
            "type": "Element",
        }
    )
    num_remedial: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumRemedial",
            "type": "Element",
        }
    )
    failure_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "FailureMethod",
            "type": "Element",
            "max_length": 64,
        }
    )
    liner_top: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LinerTop",
            "type": "Element",
        }
    )
    liner_lap: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LinerLap",
            "type": "Element",
        }
    )
    etim_before_test: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimBeforeTest",
            "type": "Element",
        }
    )
    test_negative_tool: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestNegativeTool",
            "type": "Element",
            "max_length": 64,
        }
    )
    test_negative_emw: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "TestNegativeEmw",
            "type": "Element",
        }
    )
    test_positive_tool: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestPositiveTool",
            "type": "Element",
            "max_length": 64,
        }
    )
    test_positive_emw: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "TestPositiveEmw",
            "type": "Element",
        }
    )
    cement_found_on_tool: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CementFoundOnTool",
            "type": "Element",
        }
    )
    md_dvtool: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdDVTool",
            "type": "Element",
        }
    )
    cement_job: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CementJob",
            "type": "Element",
            "required": True,
        }
    )
