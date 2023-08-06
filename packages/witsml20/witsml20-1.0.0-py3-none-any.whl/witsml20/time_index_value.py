from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_index_value import AbstractIndexValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TimeIndexValue(AbstractIndexValue):
    """
    Qualifies an index based on time.

    :ivar time: Used to specify the channel start and end index.
    """
    time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
