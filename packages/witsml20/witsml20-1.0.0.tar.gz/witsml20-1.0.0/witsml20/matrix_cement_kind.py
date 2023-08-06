from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MatrixCementKind(Enum):
    """Lithology matrix/cement description.

    The list of standard values is contained in the WITSML
    enumValues.xml file.
    """
    ANKERITE = "ankerite"
    CALCITE = "calcite"
    CHLORITE = "chlorite"
    DOLOMITE = "dolomite"
    ILLITE = "illite"
    KAOLINITE = "kaolinite"
    QUARTZ = "quartz"
    SIDERITE = "siderite"
    SMECTITE = "smectite"
