from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.abstract_object import AbstractObject
from witsml20.parameter_template import ParameterTemplate

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ActivityTemplate(AbstractObject):
    """
    Description of one type of activity.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    parameter: List[ParameterTemplate] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "min_occurs": 1,
        }
    )
