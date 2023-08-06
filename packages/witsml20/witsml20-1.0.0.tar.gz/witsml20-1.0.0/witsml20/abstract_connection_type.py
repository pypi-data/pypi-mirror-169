from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AbstractConnectionType:
    """
    The choice of connection type.
    """
