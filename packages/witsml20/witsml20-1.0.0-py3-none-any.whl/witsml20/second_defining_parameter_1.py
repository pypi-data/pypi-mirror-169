from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SecondDefiningParameter1:
    class Meta:
        name = "SecondDefiningParameter"
        namespace = "http://www.opengis.net/gml/3.2"

    inverse_flattening: Optional[float] = field(
        default=None,
        metadata={
            "name": "inverseFlattening",
            "type": "Element",
        }
    )
    semi_minor_axis: Optional[float] = field(
        default=None,
        metadata={
            "name": "semiMinorAxis",
            "type": "Element",
        }
    )
    is_sphere: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSphere",
            "type": "Element",
        }
    )
