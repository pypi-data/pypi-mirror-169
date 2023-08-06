from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_vertical_crs import AbstractVerticalCrs
from witsml20.ex_vertical_extent_type import VerticalCrstype

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalGmlCrs(AbstractVerticalCrs):
    """
    This is the Energistics encapsulation of the VerticalCrs type from GML.
    """
    gml_vertical_crs_definition: Optional[VerticalCrstype] = field(
        default=None,
        metadata={
            "name": "GmlVerticalCrsDefinition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
