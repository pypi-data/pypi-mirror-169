from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.abstract_graphical_information import AbstractGraphicalInformation
from witsml20.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GraphicalInformationSet(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    graphical_information: List[AbstractGraphicalInformation] = field(
        default_factory=list,
        metadata={
            "name": "GraphicalInformation",
            "type": "Element",
        }
    )
