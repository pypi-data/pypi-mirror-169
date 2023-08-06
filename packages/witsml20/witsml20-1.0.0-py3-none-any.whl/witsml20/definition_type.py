from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.definition_base_type import DefinitionBaseType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinitionType(DefinitionBaseType):
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
