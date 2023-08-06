from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.aggregation_type import AggregationType
from witsml20.axis import Axis
from witsml20.identified_object_type import IdentifiedObjectType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCoordinateSystemType(IdentifiedObjectType):
    axis: List[Axis] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )
