from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_index_value import AbstractIndexValue
from witsml20.abstract_log_data_context import AbstractLogDataContext

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IndexRangeContext(AbstractLogDataContext):
    """Describes the data context for a log in terms of a starting and ending
    index.

    When this context is used, each realization of the log includes all
    data points from the log's channel set that follow between the
    specified start and end index.

    :ivar start_index: When the log header defines the direction as: -
        "Increasing", the endIndex is the ending (maximum) index value
        at which the last non-null data point is located. -
        "Decreasing", the endIndex is the ending (minimum) index value
        at which the last non-null data point is located.
    :ivar end_index: When the log header defines the direction as: -
        "Increasing", the startIndex is the starting (minimum) index
        value at which the first non-null data point is located. -
        "Decreasing", the startIndex is the starting (maximum) index
        value at which the first non-null data point is located.
    """
    start_index: Optional[AbstractIndexValue] = field(
        default=None,
        metadata={
            "name": "StartIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    end_index: Optional[AbstractIndexValue] = field(
        default=None,
        metadata={
            "name": "EndIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
