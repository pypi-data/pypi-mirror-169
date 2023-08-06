from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.stim_perforation_cluster import StimPerforationCluster

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimPerforationClusterSet:
    """Provides mechanism for combining perforation clusters into a group.

    This could be used to specify the set of existing perforations
    present in a well before starting a stimulation job, for example,
    for a re-frac job.
    """
    stim_perforation_cluster: List[StimPerforationCluster] = field(
        default_factory=list,
        metadata={
            "name": "StimPerforationCluster",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
