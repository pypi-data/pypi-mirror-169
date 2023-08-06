from __future__ import annotations
from dataclasses import dataclass
from witsml20.abstract_coordinate_operation_type import AbstractCoordinateOperationType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralConversionType(AbstractCoordinateOperationType):
    pass
