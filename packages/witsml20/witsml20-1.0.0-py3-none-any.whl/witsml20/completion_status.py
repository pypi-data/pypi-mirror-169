from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class CompletionStatus(Enum):
    """
    Specifies the values of the status of a wellbore completion.
    """
    ACTIVE = "active"
    INACTIVE = "inactive"
    PERMANENTLY_ABANDONED = "permanently abandoned"
    PLANNED = "planned"
    SUSPENDED = "suspended"
    TEMPORARILY_ABANDONED = "temporarily abandoned"
    TESTING = "testing"
