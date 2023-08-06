from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimJobLogCatalog:
    """
    A group of logs from a stimulation job, one log per stage.
    """
    job_log: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "JobLog",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
