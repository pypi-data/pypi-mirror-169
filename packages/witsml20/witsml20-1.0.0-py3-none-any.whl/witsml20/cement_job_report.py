from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_cement_job import AbstractCementJob
from witsml20.cement_stage_report import CementStageReport

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CementJobReport(AbstractCementJob):
    """
    The as-built report of the job after it has been done.

    :ivar dtim_job_end: Date and time of the end of the cement job.
    :ivar dtim_job_start: Date and time of the start of the cement job.
    :ivar dtim_plug_set: Date and time that cement plug was set.
    :ivar cement_drill_out: Was the cement drilled out? Values are
        "true" (or "1") and "false" (or "0").
    :ivar dtim_cement_drill_out: Date and time that the cement was
        drilled out.
    :ivar dtim_squeeze: Date and time of a squeeze.
    :ivar dtim_pipe_rot_start: Date and time that pipe rotation started.
    :ivar dtim_pipe_rot_end: Date and time that pipe rotation started.
    :ivar dtim_recip_start: Date and time that pipe reciprocation
        started.
    :ivar dtim_recip_end: Date and time that pipe reciprocation ended.
    :ivar dens_meas_by: Method by which density is measured.
    :ivar cement_report_stage:
    """
    dtim_job_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimJobEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_job_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimJobStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_plug_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPlugSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    cement_drill_out: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CementDrillOut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dtim_cement_drill_out: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimCementDrillOut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_squeeze: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimSqueeze",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_pipe_rot_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPipeRotStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_pipe_rot_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPipeRotEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_recip_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimRecipStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_recip_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimRecipEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dens_meas_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "DensMeasBy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cement_report_stage: List[CementStageReport] = field(
        default_factory=list,
        metadata={
            "name": "CementReportStage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
