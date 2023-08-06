from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ConnectionFormType(Enum):
    """
    Specifies the values for the type of equipment-to-equipment connection.
    """
    BOX = "box"
    FLANGE = "flange"
    MANDREL = "mandrel"
    PIN = "pin"
    WELDED = "welded"
