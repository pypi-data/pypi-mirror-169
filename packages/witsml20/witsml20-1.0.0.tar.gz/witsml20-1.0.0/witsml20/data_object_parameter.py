from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_activity_parameter import AbstractActivityParameter
from witsml20.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DataObjectParameter(AbstractActivityParameter):
    """
    Parameter referencing to a top level object.
    """
    data_object: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DataObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
