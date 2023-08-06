from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AbstractWellLocation:
    """Location Schema.

    This is a location that is expressed in terms of 2D coordinates. So
    that the location can be understood, the coordinate reference system
    (CRS) must be known. The survey location is given by a pair of
    tagged values. The pairs may be: (1) latitude/longitude, (2)
    easting/northing, (3) westing/southing, (4) projectedX/projectedY,
    or (5) localX/localY. The appropriate pair must be chosen for the
    data.

    :ivar original: Flag indicating (if that Is this pair of values the
        original data given for the location? Values are "true" or "1".
        Or, if the pair of values was calculated from an original pair
        of values, set to "false" (or "0") or leave blank.
    :ivar description: A comment, generally given to help the reader
        interpret the coordinates if the CRS and the chosen pair do not
        make them clear.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: A unique identifier for a well location.
    """
    original: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Original",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
