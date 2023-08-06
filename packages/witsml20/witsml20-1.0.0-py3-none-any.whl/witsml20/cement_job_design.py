from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.abstract_cement_job import AbstractCementJob
from witsml20.cement_stage_design import CementStageDesign

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CementJobDesign(AbstractCementJob):
    """
    Design and other information about the cement job.
    """
    cement_design_stage: List[CementStageDesign] = field(
        default_factory=list,
        metadata={
            "name": "CementDesignStage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
