from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_log_data_context import AbstractLogDataContext
from witsml20.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ObjectContext(AbstractLogDataContext):
    """
    Specifies the range of index values for a log by reference to another
    object (or sub-object) which contains the index range as part of its data.

    :ivar object_reference: The context object points to another
        Energistics data object.
    :ivar sub_object_reference: If the reference is to a sub-object in a
        growing object  (e.g., a WellboreGeometry section), then this
        must contain the UID of the growing part.
    """
    object_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ObjectReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    sub_object_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubObjectReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
