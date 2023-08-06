from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractParameterKey:
    """Abstract class describing a key used to identify a parameter value.

    When multiple values are provided for a given parameter, provides a
    way to identify the parameter through its association with an
    object, a time index...
    """
